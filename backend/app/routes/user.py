from fastapi import APIRouter, Depends
from app.DTOs.UserDTO import UserDTO
from app.services.Users.UserManager import UserManager
from app.db.Database import Database

router = APIRouter(prefix="/user", tags=["user"])

def get_db():
    db = Database()
    return db

def get_user_manager(db: Database = Depends(get_db)):
    return UserManager(db)

@router.post("/add")
def add_user(
    user: UserDTO,
    user_manager: UserManager = Depends(get_user_manager)
):
    user_manager.add_user(user)
    return {"message": "User added successfully"}

@router.get("/get/email")
def get_user(
    email: str,
    user_manager: UserManager = Depends(get_user_manager)
):
    user = user_manager.get_user(email)
    if user:
        return {"message": "User found", "user": user}
    else:
        return {"message": "User not found"} 