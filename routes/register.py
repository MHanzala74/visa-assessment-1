from fastapi import APIRouter
from database.python_to_postgre import get_connection
import hashlib
from pydantic import BaseModel
from utils.security import hash_password

class RegisterSchema(BaseModel):
    username : str
    password : str

router = APIRouter()

@router.post("/register")
def register_user(data: RegisterSchema):
    try:
        conn = get_connection()
        cur = conn.cursor()

        hashed = hash_password(data.password)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
        """)

        cur.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (data.username, hashed)
        )

        conn.commit()
        return {"message": "User registered successfully"}

    except Exception as e:
        return {"error": str(e)}

    finally:
        cur.close()
        conn.close()