from fastapi import Depends, HTTPException, status
from pydantic import BaseModel
from pydantic import BaseModel
from jose import jwt, JWTError
from secrets import token_hex
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import json
import os

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET = token_hex(32)

class User(BaseModel):
    id: int
    username: str
    full_name: str
    mail: str
    disable: bool


class UserDB(User):
    password: str



def load_users (path) -> json:
    abspath = os.path.abspath(path)
    with open(abspath, "r") as users_file:
        file_contents = users_file.read()
  
    return json.loads(file_contents)