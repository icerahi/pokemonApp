from fastapi import APIRouter,Depends,HTTPException,Response
from src import models,oauth2,schemas
from src.database import pokemon_collection
from typing import List
from bson import ObjectId

router = APIRouter(tags=["Pokemon"])

#get all user's favourites pokemon
@router.get("/all",status_code=200,response_model=List[models.ShowPokemon])
def all_pokemons(current_user: models.User = Depends(oauth2.get_current_user)):
    
    all_pokemon = schemas.pokemons_serializer(pokemon_collection.find())
    return all_pokemon

#get authenticated user favourites pokemon
@router.get("/favourite_list",status_code=200, response_model=List[models.ShowPokemon])
def favourite_list(current_user: models.User = Depends(oauth2.get_current_user)):
    
    query = {"user.email":current_user.email} 
    fav_pokemons = schemas.pokemons_serializer(pokemon_collection.find(query))

    return fav_pokemons

#add new pokemon to user's favourite list
@router.post("/add",status_code=201,response_model=models.ShowPokemon)
def add_pokemon(pokemon: models.Pokemon,current_user: models.User = Depends(oauth2.get_current_user)):
    
    data =dict(pokemon)
    # data["user"]=current_user
    data['user'] =dict(current_user)
    _id = pokemon_collection.insert_one(data)
    new_pokemon = schemas.pokemon_serializer(pokemon_collection.find_one({"_id":_id.inserted_id}))
    return new_pokemon


#remote a pokemon from user's favourite list
@router.delete("/remove/{id}",status_code=204)
def remove_pokemon(id: str,current_user: models.User = Depends(oauth2.get_current_user)):
    
    pokemon = pokemon_collection.find_one({"_id":ObjectId(id)})
    
    if not pokemon:
        raise HTTPException(status_code=404, detail=f"pokemon with id '{id}' not found!!")
    if pokemon["user"]["email"] != current_user.email:
        raise HTTPException(
            status_code=401, detail=f"You are unauthorize to delete this pokemon!!"
        )
    pokemon_collection.delete_one({"_id":ObjectId(id)}
                                  )
    return Response(status_code=204)