from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host="localhost",
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("POSTGRES_USERNAME"),
        password=os.getenv("POSTGRES_PASSWORD"),
        port=os.getenv("POSTGRES_PORT")
    )
