import psycopg2
import os
import hashlib

def get_connection():
    return psycopg2.connect(
        host="localhost",
        dbname="demo",
        user=os.getenv("POSTGRES_USERNAME"),
        password=os.getenv('POSTGRES_PASSWORD'),
        port=5432
    )

def insert_data(id, name, score, visa_code, explanation):
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS employee(
                id INT PRIMARY KEY,
                name VARCHAR(40) NOT NULL,
                score INT,
                visa_code INT,
                explanation TEXT
            )
        """)

        cur.execute(
            "INSERT INTO employee (id, name, score, visa_code, explanation) VALUES (%s,%s,%s,%s,%s)",
            (id, name, score, visa_code, explanation)
        )

        conn.commit()

    except Exception as e:
        print("DB Error:", e)

    finally:
        cur.close()
        conn.close()




