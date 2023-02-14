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

oauth2 = OAuth2PasswordBearer(tokenUrl='login')

class User(BaseModel):
    id: int
    username: str
    full_name: str
    mail: str
    disable: bool


class UserDB(User):
    password: str


class UserModel():
    def __init__(self):
        self.path ="./constants/auth_users.json"
        self.exception_unauthorized = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Credenciales invalidas',
                headers={"WWW-Authenticate": "Bearer"})
            

    def load_users (self) -> json:
        abspath = os.path.abspath(self.path)
        with open(abspath, "r") as users_file:
            file_contents = users_file.read()
    
        return json.loads(file_contents)


    def search_user_db(self, username: str):
        users_db = self.load_users()
        if username in users_db:
            return UserDB(**self.users_db[username])


    def search_user(self, username: str):
        users_db = self.load_users()
        if username in users_db:
            return User(**users_db[username])
    

    def add_user(self, userDB: UserDB):
        pass


    async def auth_user(self, token: str = Depends(oauth2)):
        try:
            username = jwt.decode(token=token, key=SECRET, algorithms=[ALGORITHM]).get("sub")
            if username is None:
                raise self.exception_unauthorized
    
        except JWTError:
            raise self.exception_unauthorized

        return self.search_user(username, self.users_db)


    async def current_user(self, user: User = Depends(auth_user)):
        if user.disable:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Usuario inactivo')
        return user
        
