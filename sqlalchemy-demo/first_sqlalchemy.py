from sqlalchemy import create_engine,text
import os
print(111)

# Use environment variables for database credentials
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '3306')
DB_NAME = os.getenv('DB_NAME', 'boss_zp')

# Construct connection string securely
if not DB_PASSWORD:
    raise ValueError("DB_PASSWORD environment variable must be set")

engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

conn = engine.connect()

query = text('SELECT * FROM students')

result_set = conn.execute(query)

for row in result_set:
    print(row)
conn.close()
engine.dispose()