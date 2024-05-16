from sqlalchemy import create_engine, MetaData, Table, Column,Integer,String
from sqlalchemy.exc import CompileError
from sqlalchemy.sql import and_, or_



engine = create_engine('mysql+pymysql://root:123456@localhost:3306/boss_zp')

# 存放所有表结构定义的
meta_data = MetaData()
person = Table(
    'person', meta_data, 
    Column('phone', String(50), unique=True, primary_key=True),
    Column('name', String(50)),
    Column('age', Integer),
    Column('gender', String(50)),
)

# 在数据库中创建表
try:
    meta_data.create_all(engine)
    print("Table created successfully")
except CompileError as e:
    print(f"CompileError: {e}")
    
    
# 插入数据
# with engine.connect() as connection:
#     connection.execute(person.insert(), [
#         {"name":'John Doe1', "phone":'123-456-7891',"age":11,"gender":'male'},
#         {"name":'John Doe3', "phone":'123-456-7893',"age":11,"gender":'male'},
#         {"name":'John Doe4', "phone":'123-456-7894',"age":11,"gender":'male'},
#     ])
#     connection.commit()
    
# with engine.connect() as connection:
#     # 查询
#     s = person.select().where(
#         or_(
#             person.c.phone == '123-456-7893',
#             and_(person.c.name == 'John Doe1')
#         )
#     )
#     result_set = connection.execute(s)
#     # result = result_set.fetchone()
#     result = result_set.fetchall()
#     print(result)

# 更新
# with engine.connect() as connection:
#     u = person.update().values(gender='woman').where(person.c.phone =='123-456-7894')
#     connection.execute(u)
#     connection.commit()

# 删除
with engine.connect() as connection:
    query = person.delete().where(person.c.phone =='123-456-7893')
    connection.execute(query)
    connection.commit()
    