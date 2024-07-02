from sqlalchemy import create_engine

# Replace with your actual database URL
db_url = 'mssql+pyodbc://@DESKTOP-DREO3DI\SQLEXPRESS/db_theplotspot?driver=SQL+Server'

engine = create_engine(db_url)

# Try to connect
try:
    conn = engine.connect()
    print("Database connection successful!")
    conn.close()
except Exception as e:
    print(f"Error connecting to the database: {str(e)}")
