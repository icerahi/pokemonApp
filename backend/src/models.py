from sqlalchemy import Column,Integer,String
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class Pokemon(Base):
    __tablename__='pokemon'
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    image = Column(String)
    type = Column(String) 
    user_id = Column(Integer,ForeignKey('user.id'))
    user = relationship('User',back_populates='pokemons')


class User(Base):
    __tablename__='user' 
    id=Column(Integer,primary_key=True,index=True)
    username = Column(String)
    email = Column(String,unique=True)
    password = Column(String)
    pokemons = relationship('Pokemon',back_populates='user')

