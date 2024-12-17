import hashlib

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
    
    def add_user(self, user):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)", 
            (user.name, user.email, self.__handle_password(user.password))
        )
        conn.commit()
        self.db.close_connection(conn)
        return user
    
    def validate_password(self, email: str, password: str) -> bool:
        user = self.get_user(email)
        if not user:
            return False
        return user[3] == self.__handle_password(password)
    
    def __handle_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()