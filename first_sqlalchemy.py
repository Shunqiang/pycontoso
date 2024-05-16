from sqlalchemy import create_engine,text
print(111)
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/boss_zp')

conn = engine.connect()

query = text('SELECT * FROM students')

result_set = conn.execute(query)

for row in result_set:
    print(row)
conn.close()
engine.dispose()