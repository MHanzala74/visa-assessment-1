from schemas.profile_schema import VisaProfile
from .auth_routes import authenticate
from fastapi import APIRouter, Depends
from database.crud import profile_insert_data

router = APIRouter()

@router.post('/profile')
def user_profile(req:VisaProfile,user=Depends(authenticate)):
    first_name = req.first_name
    last_name = req.last_name
    email  = req.email
    phone = req.phone
    age = req.age
    nationality = req.nationality
    preferred_state = req.preferred_state
    current_occupation = req.current_occupation
    aus_experience = req.aus_experience
    overseas_exp = req.overseas_exp
    education_level = req.education_level
    marital_status = req.marital_status
    english_test_score = req.english_test_score
    english_test_type = req.english_test_type

    profile_insert_data(first_name,last_name,email,phone,age,nationality,preferred_state,current_occupation,aus_experience,overseas_exp,education_level,marital_status,english_test_type,english_test_score)

    return {
        "message" : "Ok"
    }
