# from database.supabase import supabase

# def save_visa_assessment(user_id, score, visa_code, explanation):
#     data = {
#         "user_id": user_id,        
#         "score": score,            
#         "visa_code": visa_code,    
#         "explanation": explanation 
#     }


#     response = supabase.table("visa_assessments").insert(data).execute()
#     return response