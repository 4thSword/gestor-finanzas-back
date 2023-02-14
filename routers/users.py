
from fastapi import APIRouter, HTTPException
from db.models.users import *


# A json file with tests data is created before database implementation

# Router definition
router = APIRouter(prefix="/user", tags=["Users"])


# Users CRUD

@router.get("/", response_model=User, status_code=200)
async def get_user(id: int):
    user_model = UserModel()
    return user_model.search_user(id)


@router.post("/", response_model=User, status_code=200)
async def add_user(user: User):
    user_model = UserModel()
    
    if type(user_model.search_user(user.id)) == User:
        raise HTTPException(404, detail=f"El usuario {user.id} ya existe")
        
    else:
        user_model.add_user()
        return user


@router.put("/", response_model=User, status_code=200)
async def update_user(user: User):
    user_model = UserModel()
    if not type(user_model.search_user(user.id)) == User:
        raise HTTPException(404, detail=f"El usuario {user.id} no existe")
    else:
        for index, saved_user in enumerate(users_list):
            if saved_user.id == user.id:
                users_list[index] = user
                return user


@router.delete("/{id}", response_model=User, status_code=200)
async def delete_user(id: int):
    if not type(search_user(id)) == User:
        raise HTTPException(404, detail=f"El usuario {id} no existe")
    else:
        for index, saved_user in enumerate(users_list):
            if saved_user.id == id:
                del users_list[index]
                return {"mensaje": f"El usuario {id} ha sido eliminado"}

