from fastapi import APIRouter,Depends,HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from src.database import user_collection
from src.hashing import Hash
from src import oauth2

router = APIRouter(tags=["Authentication"])

@router.post('/login',status_code=200)
def login(request:OAuth2PasswordRequestForm=Depends()):
    user = user_collection.find_one({"$or":[{"email":request.username},{"username":request.username}]})
    if not user:
        raise HTTPException(status_code=404,detail="Invalid Credentials")
   
    if not Hash.verify(request.password,user["password"]):
        raise HTTPException(status_code=404,detail="Incorrect Password!!")

    # generat a jwt token 
    
    access_token = oauth2.create_access_token(
        token={"email": user["email"],"username":user["username"]}
    )
    return {"access_token": access_token, "token_type": "bearer"}
    
