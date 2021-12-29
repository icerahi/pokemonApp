from typing import List, Optional
from pydantic import BaseModel
from pydantic.class_validators import validator
from pydantic.fields import Field

 


class Pokemon(BaseModel):
    name:str
    image:str
    type:str
    
 
    
class ShowUserInline(BaseModel):
    username:str 
    class Config:
        orm_mode=True
        
class ShowPokemon(Pokemon):
    id:str
    user:ShowUserInline
 
    class Config:
        orm_mode=True
        
class User(BaseModel):
    username:str
    email:str 
    password:str
    
    
class ShowUser(BaseModel):
    username:str 
    email:str 
    pokemons:List[Pokemon]=[]
    
    class Config:
        orm_mode=True
    
    
        
class TokenData(BaseModel):
    email:str 
    username:str 
    user_id:int
    
class OAuth2PasswordRequestJson(BaseModel):
    grant_type:str= Field(None,regex="password")
    username:str = Field(...)
    password:str = Field(...)
    scope:List[str]=Field(default_factory=list)
    client_id:Optional[str]=None
    client_secret:Optional[str]=None 
    
    @validator('scope',pre=True)
    def scope_from_string(cls,v):
        return v.split() if isinstance(v,str) else v 