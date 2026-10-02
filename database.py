import psycopg2
from config import settings

def get_db_connection():
    try:
        conn = psycopg2.connect(settings.DATABASE_URL)
        return conn
    except Exception as e:
        print(f"Database connection failed: {e}")
        return None

def init_db():
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS telemetry_data (
                    id SERIAL PRIMARY KEY,
                    payload JSONB,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
            cursor.close()
            conn.close()
            print("Database table 'telemetry_data' initialized successfully!")
        except Exception as e:
            print(f"Table creation error: {e}")