import os
import mysql.connector

HOST = os.environ.get('DB_HOST')
DATABASE = os.environ.get('DB_NAME')
USER = os.environ.get('DB_USER')
PASSWORD = os.environ.get('DB_PASSWORD')

def get_connection():
    return mysql.connector.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)

# CREATE
def CREATE():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))''')
        conn.commit()

def add_user(name):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
        conn.commit()

# READ
def READ():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        return cursor.fetchall()

# UPDATE
def UPDATE(user_id, new_name):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET name=%s WHERE id=%s", (new_name, user_id))
        conn.commit()
      
# DELETE
def DELETE(user_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
        conn.commit()

# DROP (for test purposes)
def DROP():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS users")
        conn.commit()

if __name__ == "__main__":
    CREATE()
