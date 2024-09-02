from fastapi import APIRouter, HTTPException
from models.user import User
from controller.user_controller import read, save, update, delete

router = APIRouter()

@router.get("/api/user/")
async def get_user_by_id(id: int):
    user = read(id)
    return user

@router.get("/api/user")
async def get_all_users():
    user = read()
    return user

@router.post("/api/user/")
async def save_user(user: User):
    try:
        return save(user)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise e

@router.put("/api/user/{id}")
async def update_user(user: User):
    is_updated = update(user)
    if is_updated:
        return user
    else:
        return "User couldn't be updated"

@router.delete("/api/user/{id}")
async def delete_user_by_id(id: int):
    is_deleted = delete(id)
    if is_deleted:
        return f"User with id {id} deleted"
    
    