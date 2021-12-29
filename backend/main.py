from typing import List
from fastapi import FastAPI, HTTPException,Depends
from sqlalchemy.orm import Session
from tortoise.expressions import Q
from src import database, models, schemas, token, oauth2
from src import hashing
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import or_
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

#tortoise orm
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()
origins =['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)


# models.Base.metadata.create_all(bind=database.engine)

get_db = database.get_db
 

@app.get("/all",status_code=200,response_model=List[schemas.ShowPokemon])
def all_pokemons(
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
   
    return db.query(models.Pokemon).all()



@app.get("/favourite_list",status_code=200, response_model=List[schemas.ShowPokemon])
def favourite_list(
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    
    pokemon = (
        db.query(models.Pokemon)
        .filter(models.Pokemon.user_id == current_user.user_id)
        .all()
    )
 
    return pokemon


@app.post("/add",status_code=201,response_model=schemas.ShowPokemon)
async def add_pokemon(
    pokemon: models.pokemon_pydanticIN,
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    
    user= await models.User.get(id=current_user.user_id)
    pokemon_obj = await models.Pokemon.create(
          name=pokemon.name,
        image=pokemon.image,
        type=pokemon.type,
        user=user,
    )
    return  pokemon_obj


@app.delete("/remove/{id}",status_code=204)
def remove_pokemon(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    pokemon = db.query(models.Pokemon).filter(models.Pokemon.id == id)
    if not pokemon.first():
        raise HTTPException(status_code=404, detail=f"pokemon with id {id} not found")
    if pokemon.first().user_id != current_user.user_id:
        raise HTTPException(
            status_code=401, detail=f"You are unauthorize to delete this pokemon!!"
        )
    pokemon.delete(synchronize_session=False)
    db.commit()
    return {"detail": "deleted successfully!!"}


# @app.post("/signup",status_code=200,response_model=schemas.ShowUser)
# def signup(request: schemas.User, db: Session=Depends(get_db)):
#     user_exists = db.query(models.User).filter(or_(models.User.email==request.username,models.User.username==request.username)).first()

#     if user_exists:
#         raise HTTPException(
#             status_code=409, detail="User already exists with this email or username!!"
#         )

#     new_user = models.User(username=request.username,email=request.email,password=Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user


# @app.post('/login',status_code=200)
# def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(database.get_db)):
#     user = db.query(models.User).filter(or_(models.User.email==request.username,models.User.username==request.username)).first()
#     if not user:
#         raise HTTPException(status_code=404,detail="Invalid Credentials")
   
#     if not Hash.verify(request.password,user.password):
#         raise HTTPException(status_code=404,detail="Incorrect Password!!")

#     # generat a jwt token 
    
#     access_token = oauth2.create_access_token(
#         token={"email": user.email,"username":user.username,'user_id':user.id}
#     )
#     return {"access_token": access_token, "token_type": "bearer"}
    
@app.post('/login',status_code=200)
async def login(request:OAuth2PasswordRequestForm=Depends()):
    user =  await models.User.filter(Q(username=request.username)|Q(email=request.username)).first()
    print(user.password)
    if not user:
        raise HTTPException(status_code=404,detail="Invalid Credentials")
   
    if not hashing.verify_password(request.password,user.password):
        raise HTTPException(status_code=404,detail="Incorrect Password!!")

    # generat a jwt token 
    
    access_token = oauth2.create_access_token(
        token={"email": user.email,"username":user.username,'user_id':user.id}
    )
    return {"access_token": access_token, "token_type": "bearer"}
    


@app.post("/signup",status_code=200,response_model=models.user_pydantic)
async def signup(user:models.user_pydanticIn):
    user_obj = await models.User.create(username=user.username,email=user.email,password=hashing.get_password_hash(user.password))
    return await models.user_pydantic.from_tortoise_orm(user_obj)




register_tortoise(app,
                  db_url="sqlite://pokemon.sqlite3",
                  modules={'models':["src.models"]},
                  generate_schemas=True,
                  add_exception_handlers=True,
                  )