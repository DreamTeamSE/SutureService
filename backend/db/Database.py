import psycopg2
from psycopg2 import sql

def connect_to_postgres_db():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="example",
            host="db",
            port="5432",
            database="suturedb"
        )
        cursor = connection.cursor()
        print("PostgreSQL connection is open")
        
        # Example query to test the connection
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")
        
        return connection, cursor

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return None, None

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
