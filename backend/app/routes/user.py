from fastapi import APIRouter, Depends, HTTPException
from app.DTOs.user.UserDTO import UserDTO
from app.DTOs.user.AuthDTO import AuthDTO
from app.services.Users.UserService import UserService
from app.db.Database import Database
from app.DAOs.UserDAO import UserDAO

router = APIRouter(prefix="/user", tags=["user"])

def get_db() -> Database:
    return Database()

def get_user_dao(db: Database = Depends(get_db)) -> UserDAO:
    return UserDAO(db)

def get_user_service(user_dao: UserDAO = Depends(get_user_dao)) -> UserService:
    return UserService(user_dao)

@router.post("/signup")
def signup(
    user: UserDTO,
    user_service: UserService = Depends(get_user_service)
):
    try:
        signup_response = user_service.signup(user)
        return signup_response
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/login")
def login(
    auth: AuthDTO,
    user_service: UserService = Depends(get_user_service)
):
    try:
        login_response = user_service.login(auth)
        if not login_response:
            return {"message": "Login was not Successful"}
        return {"message": "Login was successful"}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@router.delete("/delete")
def delete_user(
    auth: AuthDTO,
    user_service: UserService = Depends(get_user_service)
):
    try:
        deletion_response = user_service.delete_user(auth)
        return deletion_response
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Error Deleting User: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
