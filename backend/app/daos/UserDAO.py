import logging
from app.db.Database import Database
from app.DTOs.user.UserDTO import UserDTO
import bcrypt
import psycopg2
class UserDAO:
    _instance = None

    def __new__(cls, db: Database):
        if cls._instance is None:
            cls._instance = super(UserDAO, cls).__new__(cls)
            cls._instance.db = db
        return cls._instance

    def __init__(self, db: Database):
        if not hasattr(self, 'db'):
            self.db = db

    @classmethod
    def get_instance(cls, db: Database):
        if cls._instance is None:
            cls._instance = UserDAO(db)
        return cls._instance

    def get_password_hash(self, email: str) -> str:
        conn = self.db.get_connection()
        cursor = conn.cursor()
        query = "SELECT password_hash FROM users WHERE email = %s"
        params = (email,)
        cursor.execute(query, params)
        row = cursor.fetchone()

        if not row:
            raise ValueError("Email Does Not Exist")
        
        password = row[0]
        self.db.close_connection(conn)
        return password


    def hash_password(self, password: str) -> str:
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), salt).decode()

    def signup(self, user: UserDTO) -> dict:
        conn = self.db.get_connection()
        cursor = conn.cursor()
        user.password = self.hash_password(user.password)
        query = "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)"
        params = (user.name, user.email, user.password)
        try:
            cursor.execute(query, params)
            conn.commit()
            response = {
                "message": "User added successfully",
                "user": {"name": user.name, "email": user.email}
            }
        except psycopg2.errors.UniqueViolation as e:
            logging.warning(f"Error adding user: {str(e)}")
            response = {"message": "Please try a different email"}
        finally:
            self.db.close_connection(conn)
        return response
     
       
    def delete_user(self, email: str) -> dict:
        conn = self.db.get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM users WHERE email = %s RETURNING email"
        params = (email,)
        cursor.execute(query, params)
        cursor.fetchone()
        conn.commit()
        self.db.close_connection(conn)
        
        return {"message": f"{email} was deleted", "account_deleted": True}

    def _get_existing_email(self, email: str) -> bool:
        conn = self.db.get_connection()
        cursor = conn.cursor()
        query = "SELECT email FROM users WHERE email = %s"
        params = (email,)
        cursor.execute(query, params)
        existing_email = cursor.fetchone()
        self.db.close_connection(conn)
        return True if existing_email else False
