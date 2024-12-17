import bcrypt

class Response:
    def __init__(self, status="error", message="An error occurred", user=None):
        self.status = status
        self.message = message
        self.user = user

    def to_dict(self):
        return {
            "status": self.status,
            "message": self.message,
            "user": self.user
        }

class UserManager:
    def __init__(self, db):
        self.db = db
        
    def get_user(self, email):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, username, email, password_hash FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        self.db.close_connection(conn)
        return user
    
    def signup(self, user):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        password_hash = self.__handle_password(user.password)

        try:
            cursor.execute(
                "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)", 
                (user.name, user.email, password_hash)
            )
            conn.commit()
            response = Response("success", "User added successfully", user)
        except Exception as e:
            response = Response(message=str(e))
        finally:
            self.db.close_connection(conn)
        
        return response.to_dict()

    
    def login(self, user):
        if self.validate_password(user.email, user.password):
            return Response("success", "User logged in successfully", user).to_dict()
        else:
            return Response("error", "Invalid credentials").to_dict()
        
    def delete_user(self, email: str):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("DELETE FROM users WHERE email = %s", (email,))
            if cursor.rowcount == 0:
                response = Response("error", "User not found")
            else:
                conn.commit()
                response = Response("success", "User deleted successfully")
        except Exception as e:
            response = Response(message=str(e))
        finally:
            self.db.close_connection(conn)
        
        return response.to_dict()
    
    def validate_password(self, email: str, password: str) -> bool:
        user = self.get_user(email)
        if not user:
            return False
        return bcrypt.checkpw(password.encode(), user[3].encode())
    
    def __handle_password(self, password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), salt).decode()