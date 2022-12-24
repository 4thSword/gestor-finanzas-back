from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Endopoints
from accounts.endpoints import *
from labels.endpoints import *
from users.endpoints import *

# Models
from users.models import User, load_users

# A json file with tests data is created before database implementation
users_list = load_users("./constants/users.json")

# API context creation
app = FastAPI()


# Users CRUD
@app.get("/users/")
async def get_users():
    return users_list


@app.get("/user/")
async def get_user(id: int):
    return search_user(id, users_list)


@app.post("/user/")
async def add_user(user: User):
    if type(search_user(user.id)) == User:
        return {"error": f"El usuario {user.id} ya existe"}
        
    else:
        users_list.append(user)
        return user


@app.put("/user/")
async def update_user(user: User):
    if not type(search_user(user.id)) == User:
        raise HTTPException(404, detail=f"El usuario {user.id} no existe")
    else:
        for index, saved_user in enumerate(users_list):
            if saved_user.id == user.id:
                users_list[index] = user
                return user


@app.delete("/user/{id}")
async def update_user(id: int):
    if not type(search_user(id)) == User:
        return {"error": f"El usuario {id} no existe"}
    else:
        for index, saved_user in enumerate(users_list):
            if saved_user.id == id:
                del users_list[index]
                return {"mensaje": f"El usuario {id} ha sido eliminado"}


# Labels CRUD


# Accounts CRUD

