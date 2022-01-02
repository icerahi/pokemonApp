def pokemon_serializer(pokemon)->dict:
    return {
        "id":str(pokemon["_id"]),
        "name":pokemon["name"],
        "image":pokemon["image"],
        "type":pokemon["type"],
        "user":dict(pokemon["user"])
    }

def pokemons_serializer(pokemons)->list:
    return [pokemon_serializer(pokemon) for pokemon in pokemons]

def user_serializer(user)->dict:
    return {
        "id":str(user["_id"]),
        "username":user["username"],
        "email":user["email"]
    }