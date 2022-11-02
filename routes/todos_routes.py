from fastapi import APIRouter
from models.todos_model import User
from config.db import collection_name
from schemas.todos_schema import userEntity, usersEntity
from bson import ObjectId
user = APIRouter()

@user.get('/')
async def find_all_users():
    todod = usersEntity(collection_name.find())
    return {"status": "Ok", "data": todod}

@user.get('/{id}')
async def find_one_user(id: str):
    todo = userEntity(collection_name.find_one({"_id":ObjectId(id)}))
    return {"status": "Ok", "data": todo}

@user.post('/')
async def create_user(user: User):
    _id = collection_name.insert_one(dict(user))
    todo = usersEntity(collection_name.find({"_id": _id.inserted_id}))
    return {"status": "Ok", "data": todo}

@user.put('/{id}')
async def update_user(id: str, user: User):
    collection_name.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(user)
    })
    todo = usersEntity(collection_name.find({"_id":ObjectId(id)}))
    return {"status": "Ok", "data": todo}

@user.delete('/{id}')
async def delete_user(id: str, user: User):
    collection_name.find_one_and_delete({"_id":ObjectId(id)})
    return {"status": "Ok", "data": []}