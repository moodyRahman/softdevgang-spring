from pymongo import MongoClient
import json

client = MongoClient("mongodb://localhost:27017/")

db = client["test"]

collection = db["movies"]

m_count = collection.count_documents({})

if m_count == 0:
    toinsert = json.loads(open("movies.json", "r").read())
    for movie in toinsert:
        # print(type(toinsert))
        collection.insert_one(movie)


# {"title":"The Thunderbolt","year":1912,"cast":["William Garwood","James Cruze","David Thompson"],"genres":["Drama"]},

def query_title(title):
    query = {"title":{"$regex":title, "$options": "i"}}

    result = collection.find(query)

    out = []
    for movie in result:
        # print(movie)
        out.append(movie)
    return out

def query_actor(name):
    query = {"cast":{"$regex":name, "$options": "i"}}

    result = collection.find(query)

    out = []
    for actor in result:
        # print(movie)
        out.append(actor)
    return out


out = query_actor("cole")
print(out[0])
