from fastapi import FastAPI
from pydantic import BaseModel
import os
import json

app = FastAPI()

class User(BaseModel):
    id: int
    username: str
    full_name: str
    mail: str
    disable: bool
    passwd: str

def load_users (path) -> dict:
    abspath = os.path.abspath(path)
    with open(abspath, "r") as users_file:
        file_contents = users_file.read()
  
    return json.loads(file_contents)



users_db = load_users("../constants/auth_users.json")

