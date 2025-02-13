import json
import logging
import bcrypt
from app.DAOs.UserDAO import UserDAO
from app.DTOs.user.AuthDTO import AuthDTO
from app.DTOs.user.UserDTO import UserDTO

class UserService:
    def __init__(self, user_dao: UserDAO):
        self.user_dao = user_dao

    def login(self, auth: AuthDTO) -> bool:
        correct_credentials = self.validate_password(auth)
        return correct_credentials

    def validate_password(self, auth : AuthDTO) -> bool:
        try:
            password_hash = self.user_dao.get_password_hash(auth.email)
            does_password_match = bcrypt.checkpw(auth.password.encode(), password_hash.encode())
        except ValueError:
            logging.warning("Current Login Attempted Email Does Not Exist")
            return False
        return does_password_match

    def signup(self, user: UserDTO) -> dict:
        response = self.user_dao.signup(user)
        return response

    def validate_user_given_password(self, auth: AuthDTO) -> bool:
        queried_password = self.user_dao.get_password_hash(auth.email)
        password = auth.password
        return bcrypt.checkpw(password.encode(), queried_password.encode())


    def delete_user(self, auth: AuthDTO) -> dict:
        if not self.user_dao._get_existing_email(auth.email):
            return {"message": f"No occurrence of {auth.email} in database, email was not deleted", "account_deleted": False}
        
        if not self.validate_password(auth):
            return {"message": "Invalid password, account was not deleted", "account_deleted": False}
        return self.user_dao.delete_user(auth.email)
    
    

