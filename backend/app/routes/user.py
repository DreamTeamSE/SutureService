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

@router.post("/signup")
def signup(
    user: UserDTO,
    user_manager: UserManager = Depends(get_user_manager)
):
    login_response = user_manager.signup(user)
    return login_response
    

@router.post("/login")
def login(
    user: UserDTO,
    user_manager: UserManager = Depends(get_user_manager)
):
    login_response = user_manager.login(user)
    return login_response