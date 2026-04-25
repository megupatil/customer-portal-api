import sqlite3
from config import DATABASE

def get_connection():
    return sqlite3.connect(DATABASE)

def get_user(username):

    conn = get_connection()

    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username = '" + username + "'"

    cursor.execute(query)

    return cursor.fetchone()
