from sqlalchemy import create_engine, MetaData, Table, Column,Integer,String, ForeignKey,Date
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/boss_zp')
Base = declarative_base()

class Women(Base):
    __tablename__ = 'Women'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False, unique=True)
    birthday = Column(Date, nullable=False)
    adress = Column(String(255), nullable=False)
    
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)