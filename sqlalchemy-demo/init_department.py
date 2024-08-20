from sqlalchemy import create_engine, MetaData, Table, Column,Integer,String, ForeignKey
from sqlalchemy.exc import CompileError
from sqlalchemy.sql import and_, or_

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/boss_zp')

# 存放所有表结构定义的
meta_data = MetaData()

department = Table(
    'department', meta_data,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False, unique=True)
)

employee = Table(
    'employee', meta_data,
    Column("id", Integer, primary_key=True),
    Column("department_id", Integer, ForeignKey("department.id"), nullable=False),
    Column("name", String(50), nullable=False)
    
)

print(11111)

meta_data.create_all(engine)