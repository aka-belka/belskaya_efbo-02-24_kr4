from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    age: int

users=[]
id_counter = 1

@app.post("/users/")
async def create_user(user: User):
    global id_counter
    new_user = {"id": id_counter, "username": user.username, "age": user.age}
    users.append(new_user)
    id_counter+=1
    return {"message": "Create successfully!", "data": new_user}

@app.get("/users/{users_id}/")
def get_user(users_id: int):
    for user in users:
        if user["id"] == users_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{users_id}/")
def delete_user(users_id: int):
    for user in users:
        if user["id"] == users_id:
            users.remove(user)
            return {"message": "Delete successfully!"}
    raise HTTPException(status_code=404, detail="User not found")