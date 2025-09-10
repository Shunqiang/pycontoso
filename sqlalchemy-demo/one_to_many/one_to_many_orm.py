from typing import List
from sqlalchemy import create_engine, MetaData, Table, Column,Integer,String, ForeignKey,Date
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column, relationship
import datetime
from sqlalchemy.sql import func
from typing_extensions import Annotated

# Use environment variables for database credentials
import os
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '3306')
DB_NAME = os.getenv('DB_NAME', 'boss_zp')

# Construct connection string securely
if not DB_PASSWORD:
    raise ValueError("DB_PASSWORD environment variable must be set")

engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
Base = declarative_base()


int_pk = Annotated[str,  mapped_column(String(128), unique=True, nullable=False)]

default_time = Annotated[datetime.datetime, mapped_column(nullable=True, server_default=func.now())]

class Department(Base):
    __tablename__ = 'department'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[int_pk]
    create_time: Mapped[default_time]
    employees: Mapped[List['Employee']] = relationship(back_populates="department")
    def __repr__(self):
        return f'id: {self.id}, name: {self.name}, create_time:{self.create_time}'
    
    
class Employee(Base):
    __tablename__ = 'employee'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    dep_id: Mapped[int] = mapped_column(ForeignKey('department.id'))
    name: Mapped[int_pk]
    birthday: Mapped[datetime.datetime]
    department: Mapped[Department] = relationship(lazy=False, back_populates="employees")
    def __repr__(self):
        return f'id: {self.id}, dep_id: {self.dep_id}, name: {self.name}, birthday:{self.birthday}'
    
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)