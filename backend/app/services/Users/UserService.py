from app.db.Database import Database

class UserService:
    def __init__(self):
        self.db = Database()
        
    def getUser(self, email):
        conn = self.db.getConnection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        self.db.closeConnection(conn)
        return user
    
    def addUser(self, user):
        conn = self.db.getConnection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, email) VALUES (%s, %s)", (user.name, user.email))
        conn.commit()
        self.db.closeConnection(conn)
        return user
