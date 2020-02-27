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

def query_borough(borough):
    query = {"borough":borough}

    result = collection.find(query)

    out = []
    for x in result:
        out.append(x)
    return out


def query_zip(zip):
    query = {"address.zipcode":zip}

    result = collection.find(query)

    out = []
    for x in result:
        out.append(x)
    return out

def query_zip_grade(zip, grade):
    query = {"address.zipcode":zip}

    result = collection.find(query)
    out = []

    for restaurant in result:
        print(restaurant["name"])
        # print(type(x["grades"]))
        # print(x["grades"])
        for singlegrade in restaurant["grades"]:
            bad = False
            # print(singlegrade["grade"])
            if (not (singlegrade["grade"] == "Not Yet Graded") and ord(singlegrade["grade"]) <= ord(grade)):
                pass
            else:
                bad = True
        if (not bad):
            out.append(restaurant)

        print("\n")
        print("\n")
        # quit()
        return out



out = query_zip_grade("11423", "A")
