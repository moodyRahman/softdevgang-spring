import json
import sys
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")

db = client["test"]

collection = db["restaurant"]


insert = {"name":"mood", "info":{"zip":345345, "rating":5}}

# collection.insert_one(insert)


f = open("primer-dataset.json", "r")

def db_populate():
    for line in f:
        # print(type(line))
        l = line.replace("$date", "date")
        # we can process file line by line here, for simplicity I am taking count of lines
        j = json.loads(l)
        collection.insert_one(j)
