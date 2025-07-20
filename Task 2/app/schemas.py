from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    hashed_password: str
    role: Optional[str] = "user"

class RoomCreate(BaseModel):
    name: str
    description: Optional[str] = None

class MessageCreate(BaseModel):
    content: str
    user_id: int
    room_id: int

class MessageOut(BaseModel):
    id: int
    content: str
    timestamp: datetime
    user_id: int
    room_id: int

    class Config:
        orm_mode = True
