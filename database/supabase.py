from supabase import create_client
from dotenv import load_dotenv
load_dotenv()
import os 

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

supabase = create_client(SUPABASE_URL,SUPABASE_KEY)