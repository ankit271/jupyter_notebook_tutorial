
from typing import Union
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI();
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

users = [
    {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "age": 30
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "email": "jane.smith@example.com",
        "age": 25
    },
    {
        "id": 3,
        "name": "Bob Johnson",
        "email": "bob.johnson@example.com",
        "age": 35
    }
]

@app.get('/')
def say_hello():
    return {"message": "Hello World!"}


@app.get("/users")
async def list_users(request: Request):
    users = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
    ]
    return templates.TemplateResponse(
        "users/user.html",
        {"request": request, "users": users}
    )


# @app.get('/users')
# def get_users():
#     return {"users": users}

@app.get('/users/{user_id}')
def get_user(user_id: int):
    for user in users:
        if user['id'] == user_id:
            return {"user": user}
    return {"error": "User not found"}


@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}


@app.post("/user/")
async def create_user(name: str, email: str, age: int):
    new_user = {
        "id": len(users) + 1,
        "name": name,
        "email": email,
        "age": age
    }
    users.append(new_user)
    return {"user": new_user}