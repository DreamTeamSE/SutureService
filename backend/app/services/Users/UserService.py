from app.db.Database import Database

class UserService:
    def __init__(self):
        self.db = Database()

    def getUser(self, id):
        conn = self.db.getConnection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
        user = cursor.fetchone()
        self.db.closeConnection(conn)
        return user
    
    def addUser(self, user):
        conn = self.db.getConnection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (id, name) VALUES (%s, %s)", (user.id, user.name))
        conn.commit()
        self.db.closeConnection(conn)
        return user
