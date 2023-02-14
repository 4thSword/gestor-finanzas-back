from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from passlib.context import CryptContext
from datetime import datetime, timedelta

from db.models.users import *

router = APIRouter(prefix="/users", tags=["Auth"])
crypt = CryptContext(schemes="bcrypt")


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_model = UserModel()
    users_db = user_model.load_users()

    user_db = users_db.get(form.username)

    if not user_db:
        raise HTTPException(
            status_code=400, 
            detail='Usuario incorrecto'
            )
    user = user_model.search_user_db(form.username)
    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=400, 
            detail='Contraseña incorrecta'
            )

    expire = datetime.utcnow + timedelta(minutes=ACCESS_TOKEN_DURATION)
    access_token = {
        "sub":user.username, 
        "exp":expire,
        }

    return {
        "acces_token": jwt.encode(
            access_token, 
            SECRET,
            algorithm=ALGORITHM
            ),
        "token_type": "bearer"
        }


@router.get("/users/me")
async def me(user: User):
    user_model = UserModel()
    user = Depends(user_model.current_user)
    return user
