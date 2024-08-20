from typing import List
from sqlalchemy import create_engine, MetaData, Table, Column,Integer,String, ForeignKey,Date
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column, relationship
import datetime
from sqlalchemy.sql import func
from typing_extensions import Annotated

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/boss_zp')
Base = declarative_base()


int_pk = Annotated[str,  mapped_column(String(128), unique=True, nullable=False)]

default_time = Annotated[datetime.datetime, mapped_column(nullable=True, server_default=func.now())]

# association_table = Table(
#     "user_role",
#     Base.metadata,
#     Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
#     Column("role_id", Integer, ForeignKey("roles.id"), primary_key=True)
# )

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    password: Mapped[int] = mapped_column()

    name: Mapped[int_pk]
    roles: Mapped[List['Role']] = relationship(lazy=False, back_populates='users')
    def __repr__(self):
        return f'id: {self.id}, name: {self.name}'
    
    
class Role(Base):
    __tablename__ = 'roles'
    role_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[int_pk]
    users: Mapped[User] = relationship(lazy=False, back_populates='roles')
    def __repr__(self):
        return f'id: {self.id},name: {self.name},'
    
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)