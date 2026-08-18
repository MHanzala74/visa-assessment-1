from dotenv import load_dotenv
import psycopg2
import os
from .connection import get_connection

load_dotenv()

# Authentication 
def create_users_table():
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

    finally:
        cur.close()
        conn.close()


def get_user_by_username(username: str):
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
        return {
            "username": user[0],
            "password": user[1]
        }
    return None

def create_user(username: str, password: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s)",
        (username, password)
    )

    conn.commit()
    cur.close()
    conn.close()



# Fetch user 
def get_employee_by_phone(phone):
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT
                first_name,
                last_name,
                email,
                phone,
                age,
                nationality,
                preferred_state,
                current_occupation,
                aus_experience,
                overseas_exp,
                education_level,
                marital_status,
                english_test_type,
                english_test_score
            FROM userprofile
            WHERE phone = %s
        """, (phone,))

        row = cur.fetchone()
        if not row:
            return None

        return {
            "first_name": row[0],
            "last_name": row[1],
            "email": row[2],
            "phone": row[3],
            "age": row[4],
            "nationality": row[5],
            "preferred_state": row[6],
            "current_occupation": row[7],
            "aus_experience": row[8],
            "overseas_exp": row[9],
            "education_level": row[10],
            "marital_status": row[11],
            "english_test_type": row[12],
            "english_test_score": row[13]
        }

    finally:
        cur.close()
        conn.close()

def create_table_if_not_exists():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS userdetail (
        id SERIAL PRIMARY KEY,
        user_name VARCHAR(100) NOT NULL,
        score INTEGER NOT NULL,
        subclass VARCHAR(50)
    );
    """)

    conn.commit()
    cur.close()
    conn.close()

def insert_data(user_name, score, subclass):
    conn = get_connection()
    cur = conn.cursor()

    query = """
    INSERT INTO userdetail (user_name, score, subclass)
    VALUES (%s, %s, %s)
    """

    cur.execute(query, (user_name, score, subclass))
    conn.commit()

    cur.close()
    conn.close()


def profile_insert_data(
    first_name,
    last_name,
    email,
    phone,
    age,
    nationality,
    preferred_state,
    current_occupation,
    aus_experience,
    overseas_exp,
    education_level,
    marital_status,
    english_test_type,
    english_test_score
):
    try:
        conn = get_connection()
        cur = conn.cursor()

        # Create table if not exists
        cur.execute("""
            CREATE TABLE IF NOT EXISTS userprofile (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                email VARCHAR(100),
                phone VARCHAR(20),
                age INT,
                nationality VARCHAR(50),
                preferred_state VARCHAR(50),
                current_occupation VARCHAR(50),
                aus_experience INT,
                overseas_exp INT,
                education_level VARCHAR(50),
                marital_status VARCHAR(50),
                english_test_type VARCHAR(20),
                english_test_score FLOAT
            )
        """)

        # Insert data
        cur.execute("""
            INSERT INTO userprofile (
                first_name, last_name, email, phone, age,
                nationality, preferred_state, current_occupation,
                aus_experience, overseas_exp, education_level,
                marital_status, english_test_type, english_test_score
            )
            VALUES (%s, %s, %s, %s, %s,
                    %s, %s, %s,
                    %s, %s, %s,
                    %s, %s, %s)
        """, (
            first_name,
            last_name,
            email,
            phone,
            age,
            nationality,
            preferred_state,
            current_occupation,
            aus_experience,
            overseas_exp,
            education_level,
            marital_status,
            english_test_type,
            english_test_score
        ))

        conn.commit()
        print("Data inserted successfully")

    except Exception as e:
        print("DB Error:", e)

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
            