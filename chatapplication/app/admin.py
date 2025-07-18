from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.dependencies import require_role, get_db
from app import models

router = APIRouter(prefix="/admin", tags=["admin"])

@router.get("/users")
def list_users(db: Session = Depends(get_db), user=Depends(require_role("admin"))):
    users = db.query(models.User).all()
    return [{"id": u.id, "username": u.username, "role": u.role} for u in users]

@router.get("/rooms")
def list_rooms(db: Session = Depends(get_db), user=Depends(require_role("admin"))):
    # Assuming chat rooms are identified by distinct room_ids in messages table
    rooms = db.query(models.Message.room_id).distinct().all()
    return [r[0] for r in rooms]

@router.delete("/messages/{message_id}")
def delete_message(message_id: int, db: Session = Depends(get_db), user=Depends(require_role("admin"))):
    msg = db.query(models.Message).filter(models.Message.id == message_id).first()
    if not msg:
        raise HTTPException(status_code=404, detail="Message not found")
    db.delete(msg)
    db.commit()
    return {"detail": "Message deleted"}

@router.put("/messages/{message_id}")
def edit_message(message_id: int, content: str, db: Session = Depends(get_db), user=Depends(require_role("admin"))):
    msg = db.query(models.Message).filter(models.Message.id == message_id).first()
    if not msg:
        raise HTTPException(status_code=404, detail="Message not found")
    msg.content = content
    db.commit()
    return {"detail": "Message updated"}

@router.put("/users/{user_id}/role")
def change_user_role(user_id: int, new_role: str, db: Session = Depends(get_db), user=Depends(require_role("admin"))):
    user_obj = db.query(models.User).filter(models.User.id == user_id).first()
    if not user_obj:
        raise HTTPException(status_code=404, detail="User not found")
    if new_role not in ("admin", "user"):
        raise HTTPException(status_code=400, detail="Invalid role")
    user_obj.role = new_role
    db.commit()
    return {"detail": f"User role changed to {new_role}"}
