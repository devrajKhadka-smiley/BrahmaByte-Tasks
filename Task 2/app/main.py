from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import engine, get_db
from app import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/users/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.post("/rooms/")
def create_room(room: schemas.RoomCreate, db: Session = Depends(get_db)):
    return crud.create_room(db, room)

@app.post("/messages/")
def create_message(message: schemas.MessageCreate, db: Session = Depends(get_db)):
    return crud.create_message(db, message)

@app.get("/rooms/{room_id}/messages/", response_model=list[schemas.MessageOut])
def get_messages(room_id: int, db: Session = Depends(get_db)):
    return crud.get_messages_by_room(db, room_id)
