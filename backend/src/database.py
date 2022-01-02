from pymongo import MongoClient 


client = MongoClient("mongodb+srv://icerahi:icerahi@cluster0.6bjxg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client.pokemon_application

pokemon_collection = db['favourite_pokemon']
user_collection =db['users']