import os
from psycopg2.pool import SimpleConnectionPool
from dotenv import load_dotenv

load_dotenv()

DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_NAME = os.getenv("DATABASE_NAME")

class Database:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'pool'):
            self.pool = SimpleConnectionPool(
                1, 50,
                user="admin",
                password="admin",
                host="db",
                port=5432,
                database="suturedb"
            )

    def get_connection(self):
        return self.pool.getconn()

    def close_connection(self, conn):
        self.pool.putconn(conn)