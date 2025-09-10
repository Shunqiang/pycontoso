from sqlalchemy import create_engine, MetaData, Table, Column,Integer,String, ForeignKey,Date
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy.orm import sessionmaker
import os

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
Base = declarative_base()

class Women(Base):
    __tablename__ = 'Women'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False, unique=True)
    birthday = Column(Date, nullable=False)
    adress = Column(String(255), nullable=False)
    
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)