from pydantic import BaseModel
import json

class User(BaseModel):
    id: int
    name: str
    surname: str
    mail: str
    passwd: str


def load_users (path) -> list:
    users_list = []
    with open(path, "r") as users_file:
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
