from fastapi import WebSocket, WebSocketDisconnect, Depends, status, APIRouter
from jose import jwt, JWTError
from typing import List
from .database import get_db
from . import models
from sqlalchemy.orm import Session
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

# ------------------------
# Connection Manager Class
# ------------------------
class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[str, List[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, room_id: str):
        await websocket.accept()
        if room_id not in self.active_connections:
            self.active_connections[room_id] = []
        self.active_connections[room_id].append(websocket)

    def disconnect(self, websocket: WebSocket, room_id: str):
        if room_id in self.active_connections:
            if websocket in self.active_connections[room_id]:
                self.active_connections[room_id].remove(websocket)
                if not self.active_connections[room_id]:
                    del self.active_connections[room_id]

    async def broadcast(self, room_id: str, message: dict):
        for connection in self.active_connections.get(room_id, []):
            await connection.send_json(message)

manager = ConnectionManager()

# ------------------------
# Utility Functions
# ------------------------
def decode_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {
            "username": payload.get("sub"),
            "role": payload.get("role")
        }
    except JWTError:
        raise ValueError("Invalid token")

async def fetch_recent_messages(db: Session, room_id: str, limit: int = 20):
    return db.query(models.Message)\
        .filter(models.Message.room_id == room_id)\
        .order_by(models.Message.timestamp.desc())\
        .limit(limit)\
        .all()

async def save_message(db: Session, content: str, room_id: str, user_id: int):
    new_msg = models.Message(
        content=content,
        room_id=room_id,
        timestamp=datetime.utcnow(),
        user_id=user_id
    )
    db.add(new_msg)
    db.commit()
    db.refresh(new_msg)
    return new_msg

# ------------------------
# WebSocket Endpoint
# ------------------------
router = APIRouter()

@router.websocket("/ws/{room_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    room_id: str,
    token: str,
    db: Session = Depends(get_db)
):
    try:
        # Validate token and get user
        user_data = decode_token(token)
        user = db.query(models.User).filter(models.User.username == user_data["username"]).first()
        if not user:
            await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
            return

        await manager.connect(websocket, room_id)

        # Send recent messages on connection
        recent = await fetch_recent_messages(db, room_id)
        for msg in reversed(recent):  # oldest first
            await websocket.send_json({
                "user": msg.sender.username,
                "message": msg.content,
                "timestamp": msg.timestamp.isoformat()
            })

        # Chat loop
        while True:
            try:
                data = await websocket.receive_json()
                message_text = data.get("message")
                if not message_text:
                    await websocket.send_json({"error": "Message content is required."})
                    continue

                saved_msg = await save_message(db, message_text, room_id, user.id)

                await manager.broadcast(room_id, {
                    "user": user.username,
                    "message": saved_msg.content,
                    "timestamp": saved_msg.timestamp.isoformat()
                })

            except Exception as json_error:
                await websocket.send_json({"error": "Invalid JSON format."})
                continue

    except WebSocketDisconnect:
        manager.disconnect(websocket, room_id)

    except Exception as e:
        print("WebSocket error:", str(e))
        await websocket.close(code=1011)
