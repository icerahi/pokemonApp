from fastapi import Depends,HTTPException,security
from datetime import datetime,timedelta
from jose import jwt,JWTError
from src import schemas

oauth2_scheme = security.OAuth2PasswordBearer(tokenUrl='login')



SECRET_KEY=''
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPORE_MUNITES=30

def create_access_token(token:dict):
    to_encode = token.copy()
    expire = datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPORE_MUNITES)
    
    to_encode.update({'exp':expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,ALGORITHM)
    return encoded_jwt




def get_current_user(token:str=Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail='Could not validate credentials',
        headers={"WWW-Authenticate":"Bearer"},
    )
    try:
        payload = jwt.decode(token,SECRET_KEY,ALGORITHM)
        email:str = payload.get('email')
        username:str = payload.get('username')
        user_id:int = payload.get('user_id')
        if email is None or username is None:
            raise credentials_exception
        
        return schemas.TokenData(email=email,username=username,user_id=user_id)
   
    except JWTError:
        raise credentials_exception