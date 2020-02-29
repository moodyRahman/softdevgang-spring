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
    """Store a query for execution"""

    def __init__(self):
        super(Query, self).__init__()
        self.query = {"$and":[]}
        self.query_out = []

    def genre(self, g):
        self.query["$and"].append({"genre":{"$regex":g, "$options": "i"}})
        return self

    def title(self, g):
        self.query["$and"].append({"title":{"$regex":g, "$options": "i"}})
        return self

    def actor(self, g):
        self.query["$and"].append({"cast":{"$regex":g, "$options": "i"}})
        return self

    def beforeyear(self, g):
        self.query["$and"].append({"year":{"$lte":g}})
        return self

    def afteryear(self, g):
        self.query["$and"].append({"year":{"$gte":g}})
        return self


    def execute(self):
        out = []
        result = collection.find(self.query)
        for x in result:
            out.append(x)
        self.query_out = out[:]
        return out

    def pretty_print(self):
        return self.query.copy()


q = Query()

q.actor("michael").afteryear(1999).beforeyear(2001)
print(q.pretty_print())
d = q.execute()
#
g = q.query_out

print(d)
print("\n\n\n\n\n")
print(g)

print(len(d))
