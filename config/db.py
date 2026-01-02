from dotenv import load_dotenv
import psycopg2
import os
import hashlib

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host="localhost",
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("POSTGRES_USERNAME"),
        password=os.getenv("POSTGRES_PASSWORD"),
        port=os.getenv("POSTGRES_PORT")
    )

def create_table(username: str, password: str):
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(100) UNIQUE NOT NULL,
                password TEXT NOT NULL
            );
        """)

        conn.commit()
        print("User inserted successfully")

    except Exception as e:
        print(f"DB ERROR: {e}")

    finally:
        cur.close()
        conn.close()

def get_user_by_username(username:str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT username, password FROM users WHERE username=%s",
        (username,)
    )
    user = cur.fetchone()
    cur.close()
    conn.close()

    if user:
        return{
            "username":user[0],
            "password":user[1]
        }
    return None


def create_user(username:str,password:str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO users (username,password) VALUES (%s, %s)",
        (username,password)
    )

    conn.commit()
    cur.close()
    conn.close()
