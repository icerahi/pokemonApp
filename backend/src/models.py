# from sqlalchemy import Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship
# from src.database import Base

# class Pokemon(Base):
#     __tablename__='pokemons'
#     id = Column(Integer,primary_key=True,index=True)
#     name = Column(String)
#     image = Column(String)
#     type = Column(String) 
#     user_id = Column(Integer,ForeignKey('users.id'))
#     user = relationship('User',back_populates='pokemons')


# class User(Base):
#     __tablename__='users' 
#     id=Column(Integer,primary_key=True,index=True)
#     username = Column(String)
#     email = Column(String,unique=True)
#     password = Column(String)
#     pokemons = relationship('Pokemon',back_populates='user')


from tortoise.models import Model
from tortoise import fields 
from tortoise.contrib.pydantic import pydantic_model_creator

class Pokemon(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=30,nullable=False)
    image = fields.CharField(max_length=300,nullable=False)
    type = fields.CharField(max_length=50,nullable=False)
    user = fields.ForeignKeyField('models.User',related_name='added_by')
    
class User(Model):
    id= fields.IntField(pk=True)
    username = fields.CharField(max_length=20)
    email = fields.CharField(max_length=100)
    password = fields.TextField()
    # pokemons = relationship('Pokemon',back_populates='user')
 
        
# create pydantic models 
pokemon_pydantic = pydantic_model_creator(Pokemon,name="Pokemon")
pokemon_pydanticIN = pydantic_model_creator(Pokemon,name="PokemonIn",exclude_readonly=True)

user_pydantic = pydantic_model_creator(User,name="User",exclude=["password"])
user_pydanticIn = pydantic_model_creator(User,name="UserIn",exclude_readonly=True)
