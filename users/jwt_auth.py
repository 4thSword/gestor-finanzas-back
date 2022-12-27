from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from passlib.context import CryptContext
from datetime import datetime, timedelta

from users.users_models import *

router = APIRouter(prefix="/users", tags=["Auth"])
oauth2 = OAuth2PasswordBearer(tokenUrl='login')
crypt = CryptContext(schemes="bcrypt")


users_db = load_users("./constants/auth_users.json")

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])


def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])


async def auth_user(token: str = Depends(oauth2)):
    exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Credenciales invalidas',
            headers={"WWW-Authenticate": "Bearer"})
            
    try:
        username = jwt.decode(token=token, key=SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception
    
    except JWTError:
        raise exception

    return search_user(username)


async def current_user(user: User = Depends(auth_user)):
    if user.disable:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Usuario inactivo')
    return user
    

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=400, 
            detail='Usuario incorrecto'
            )
    user = search_user_db(form.username)
    print(user)
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
async def me(user: User = Depends(current_user)):
    return user
