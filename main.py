from fastapi import FastAPI, HTTPException
from models import User, Gender, Role
from typing import List
from uuid import uuid4, UUID


app = FastAPI()

db: List[User] = [

    User(
          id = UUID("6b63f3cc-1057-4637-a57e-638e40ac768c"),
          first_name = "Oleh",
          last_name = "Kurza",
          gender = Gender.male,
          roles=[Role.student] 
          ),

    User(
          id = UUID("6d9fc7b8-0f34-46e0-804e-bc7d74c6a398"),
          first_name = "Jeff",
          last_name = "Misner",
          gender = Gender.male,
          roles=[Role.user, Role.admin]
          )

]


@app.get("/")
async def root():
    return {"message": "Hello Oleh"} 

@app.get ("/api/v1/users")
async def fetch_user ():
    return db;

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id":user.id}

@app.delete("/api/v1/users")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
