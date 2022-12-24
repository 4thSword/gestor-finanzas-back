
from fastapi import APIRouter, HTTPException
from users.users_models import load_users, search_user, User


# A json file with tests data is created before database implementation
users_list = load_users("./constants/users.json")


# Router definition
router = APIRouter(prefix="/users", tags=["Users"])


# Users CRUD
@router.get("/list/", response_model=list[User])
async def list_users():
    return users_list


@router.get("/user/", response_model=User, status_code=200)
async def get_user(id: int):
    return search_user(id, users_list)


@router.post("/user/", response_model=User, status_code=200)
async def add_user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(404, detail=f"El usuario {user.id} ya existe")
        
    else:
        users_list.append(user)
        return user


@router.put("/user/", response_model=User, status_code=200)
async def update_user(user: User):
    if not type(search_user(user.id)) == User:
        raise HTTPException(404, detail=f"El usuario {user.id} no existe")
    else:
        for index, saved_user in enumerate(users_list):
            if saved_user.id == user.id:
                users_list[index] = user
                return user


@router.delete("/user/{id}", response_model=User, status_code=200)
async def delete_user(id: int):
    if not type(search_user(id)) == User:
        raise HTTPException(404, detail=f"El usuario {id} no existe")
    else:
        for index, saved_user in enumerate(users_list):
            if saved_user.id == id:
                del users_list[index]
                return {"mensaje": f"El usuario {id} ha sido eliminado"}

