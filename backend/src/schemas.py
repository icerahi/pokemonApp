from typing import List
from pydantic import BaseModel

 


class Pokemon(BaseModel):
    name:str
    image:str
    type:str
    
 
    
class ShowUserInline(BaseModel):
    username:str 
    class Config():
        orm_mode=True
        
class ShowPokemon(Pokemon):
    user:ShowUserInline
 
    class Config():
        orm_mode=True
        
class User(BaseModel):
    username:str
    email:str 
    password:str
    
    
class ShowUser(BaseModel):
    username:str 
    email:str 
    pokemons:List[Pokemon]=[]
    
    class Config():
        orm_mode=True
    
    
        
class TokenData(BaseModel):
    email:str 
    username:str 
    user_id:int