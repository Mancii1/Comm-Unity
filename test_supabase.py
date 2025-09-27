import psycopg2

try:
    conn = psycopg2.connect(
        "postgresql://postgres:ageraR541*&*@db.hlepctfmkfqfqsztpswg.supabase.co:5432/postgres?sslmode=require"
    )
    print("Connected to Supabase!")
    conn.close()
except Exception as e:
    print("Connection failed:", e)
