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


class Query(object):
    """docstring for Query."""

    def __init__(self):
        super(Query, self).__init__()
        self.query = {}

    def genre(self, g):
        self.query["genre"] = {"$regex":g, "$options": "i"}
        return self

    def title(self, g):
        self.query["title"] = {"$regex":g, "$options": "i"}
        return self

    def actor(self, g):
        self.query["cast"] = {"$regex":g, "$options": "i"}
        return self

    def beforeyear(self, g):
        self.query["year"] = {"$lte":g}
        return self

    def afteryear(self, g):
        self.query["year"] = {"$gte":g}
        return self


    def execute(self):
        out = []
        result = collection.find(self.query)
        for x in result:
            out.append(x)
        return out


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
    print(query)

    result = collection.find(query)

    out = []
    for actor in result:
        # print(movie)
        out.append(actor)
    return out


def query_after_year(year):
    query = {"year":{"$gte":year}}

    result = collection.find(query)

    out = []
    for year in result:
        # print(movie)
        out.append(year)
    return out

def query_before_year(year):
    query = {"year":{"$lte":year}}

    result = collection.find(query)

    out = []
    for year in result:
        # print(movie)
        out.append(year)
    return out

def query_genre(genre):
    query = {"genres":{"$regex":genre, "$options": "i"}}

    result = collection.find(query)

    out = []
    for g in result:
        # print(movie)
        out.append(g)
    return out


q = Query()

q.actor("brian").afteryear(2010)
print(q.query)
d = q.execute()

for x in d:
    print(x)
