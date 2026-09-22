from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class User(BaseModel):
    name: str
    age: int
    email: str


users = [ ]

next_id = 0

@app.get("/users")
async def get_users(name: str | None = None):
    if name:
        result = []

        for user in users:
            if user["name"].lower() == name.lower():
                result.append(user)

        return result

    return users


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user

    

@app.post("/users")
async def create_user(user: User):
    global next_id

    new_user = {
        "id": next_id,
        "name": user.name,
        "age": user.age,
        "email": user.email
    }

    users.append(new_user)
    next_id += 1

    return new_user


@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    for existing_user in users:
        if existing_user["id"] == user_id:
            existing_user["name"] = user.name
            existing_user["age"] = user.age
            existing_user["email"] = user.email

            return existing_user


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)

            return {"Пользователь удалён"}
