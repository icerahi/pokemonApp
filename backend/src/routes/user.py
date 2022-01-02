from fastapi import APIRouter,HTTPException
from src import models,schemas
from src.database import user_collection
from src.hashing import Hash

router = APIRouter(tags=["user"])

@router.post("/signup",status_code=200)
def signup(user: models.User):
    
    user_exist = user_collection.find_one({"$or":[{"email":user.email},{"username":user.username}]})
   
    if user_exist is not None:
        raise HTTPException(
            status_code=409, detail="User already exists with this Credentials.Username and Email must be unique!!"
        )
        
    user.password = Hash.bcrypt(user.password)
    _id = user_collection.insert_one(dict(user))
    new_user = schemas.user_serializer(user_collection.find_one({"_id":_id.inserted_id}))

    return new_user
