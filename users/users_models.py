from pydantic import BaseModel
import json
import os

class User(BaseModel):
    id: int
    name: str
    surname: str
    mail: str
    passwd: str


def load_users (path) -> list:
    users_list = []
    abspath = os.path.abspath(path)
    with open(abspath, "r") as users_file:
        file_contents = users_file.read()
  
    parsed_json = json.loads(file_contents)
    for user in parsed_json:
        users_list.append(User(id=user["id"], 
                               name=user["name"], 
                               surname=user["surname"],
                               mail=user['mail'],
                               passwd=user["passwd"]
                               )
                         )

    return users_list


def search_user(id, users_list):
    current_user = list(filter(lambda user: user.id == id, users_list))
    try:
        return current_user[0]
    except:
        return None