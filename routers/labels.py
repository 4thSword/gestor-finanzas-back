from fastapi import APIRouter, HTTPException
from db.models.labels import *
from db.models.users import UserModel, User

# A json file with tests data is created before database implementation
# labels_list = load_labels("./constants/auth_users.json")


# Router definition
router = APIRouter(prefix="/labels", tags=["Labels"])


# CRUD labels
@router.get("/list/{user_id}", response_model=list[Label])
async def list_labels(user_id: int):
    pass


@router.get("/{user_id}/{label_id}", response_model=Label, status_code=200)
async def get_label(user_id: int, label_id: int):
    pass


@router.post("/{user_id}", response_model=Label, status_code=200)
async def add_label(user_id: int, label: Label):
    pass


@router.put("/{user_id}/{label_id}", response_model=Label, status_code=200)
async def update_label(user_id: int, label: Label):
   pass


@router.delete("/{user_id}/{label_id}", response_model=Label, status_code=200)
async def delete_label(user_id: int, id: int):
   pass


@router.delete("/{user_id}/{label_id}/{value_id}}", response_model=Label, status_code=200)
async def delete_label_value(user_id: int, label_id: int, value_id: int):
   pass
