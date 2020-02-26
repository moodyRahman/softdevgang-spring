
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")

db = client["test"]

collection = db["restaurant"]


insert = {"name":"mood", "info":{"zip":345345, "rating":5}}

collection.insert_one(insert)




print(type(db))
