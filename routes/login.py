from fastapi import APIRouter, HTTPException
from database.python_to_postgre import get_connection
from utils.security import verify_password
from utils.jwt import create_token
from pydantic import BaseModel

class LoginSchema(BaseModel):
    username: str
    password: str

router = APIRouter()

@router.post("/login")
def login_user(data: LoginSchema):
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "SELECT password FROM users WHERE username = %s",
            (data.username,)
        )
        user = cur.fetchone()

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        if not verify_password(data.password, user[0]):
            raise HTTPException(status_code=401, detail="Wrong password")

        token = create_token({"sub": data.username})

        return {
            "message": "Login successful",
            "access_token": token,
            "token_type": "bearer"
        }

    finally:
        cur.close()
        conn.close()
