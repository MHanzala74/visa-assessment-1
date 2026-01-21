from fastapi import APIRouter, HTTPException, Depends
from services.auth_service import hash_password, verify_password
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from schemas.auth_schema import SignupRequest
from database.crud import get_user_by_username, create_user , create_users_table

router = APIRouter()
security = HTTPBasic()

def authenticate(credentials:HTTPBasicCredentials=Depends(security)):
    user = get_user_by_username(credentials.username)

    if not user or not verify_password(credentials.password,user['password']):
        raise HTTPException(status_code=401,detail="Invalid creadentials")
    return {
        "username":user["username"]
    }

@router.post('/signup')
def signup(req:SignupRequest):
    create_users_table()
    existing_user = get_user_by_username(req.username)
    if existing_user:
        raise HTTPException(status_code=400,detail="User already exists")
    
    hashed_pw = hash_password(req.password)
    create_user(req.username, hashed_pw)

    return {"message":"User Created Successfully"}


@router.get('/login')
def login(user = Depends(authenticate)):
    return{
        "message":f"Welcome {user['username']}",
        
    }