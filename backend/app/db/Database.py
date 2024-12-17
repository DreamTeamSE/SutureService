from psycopg2.pool import SimpleConnectionPool

class Database:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'pool'):
            self.pool = SimpleConnectionPool(1, 50, user="admin", password="admin", host="db", port=5432, database="suturedb")

    def getConnection(self):
        return self.pool.getconn()

    def closeConnection(self, conn):
        self.pool.putconn(conn)