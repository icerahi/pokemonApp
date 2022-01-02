from pydantic import BaseModel

class User(BaseModel):
    username:str
    email:str 
    password:str 
    
class ShowUser(BaseModel):
    username:str 
    email:str
    

class Pokemon(BaseModel):
    name:str
    image:str
    type:str 
    
    
class ShowPokemon(Pokemon):
    id:str
    user:ShowUser
    class Config:
        orm_mode=True
    
    

class TokenData(BaseModel):
    email:str 
    username:str 
    
