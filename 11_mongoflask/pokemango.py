from pymongo import MongoClient
import json

client = MongoClient("mongodb://localhost:27017/")

db = client["test"]

pokedb = db["pokemon"]
p_count = pokedb.count_documents({})

if p_count == 0:
	toinsert = json.loads(open("poke.json", "r").read())
	allmons = toinsert["pokemon"]
	for poke in allmons:
		# print(type(toinsert))
		pokedb.insert_one(poke)


#   "id": 129,
	#   "num": "129",
	#   "name": "Magikarp",
	#   "img": "http://www.serebii.net/pokemongo/pokemon/129.png",
	#   "type": [
	#     "Water"
	#   ],
	#   "height": "0.89 m",
	#   "weight": "10.0 kg",
	#   "candy": "Magikarp Candy",
	#   "candy_count": 400,
	#   "egg": "2 km",
	#   "spawn_chance": 4.78,
	#   "avg_spawns": 478,
	#   "spawn_time": "14:26",
	#   "multipliers": [
	#     10.1,
	#     11.8
	#   ],
	#   "weaknesses": [
	#     "Electric",
	#     "Grass"
	#   ],
	#   "next_evolution": [{
	#     "num": "130",
	#     "name": "Gyarados"
	#   }]

class PokeQuery(object):
	"""Create a query to be executed

	Attributes
	----------
	query : dict
			inner query dictionary
	query_out : list
			stores the out of an execute()

	"""

	def __init__(self):
		""" Initialize a query """
		super(PokeQuery, self).__init__()
		self.query = {"$and": []}
		self.query_out = []

	def num(self, num):
		"""Specify a poke number to search the database by

		Parameters
		----------
		num : int
				pokeno to query by

		Returns
		-------
		Query
				this instance of Query

		"""
		num = str(num)
		self.query["$and"].append({"num": {"$regex": num, "$options": "i"}})
		return self

	def type(self, element):
		self.query["$and"].append({"type": {"$regex": element, "$options": "i"}})
		return self

	def weakto(self, type):
		self.query["$and"].append({"weaknesses": {"$regex": type, "$options": "i"}})

	def name(self, name):
		self.query["$and"].append({"name": {"$regex": name, "$options": "i"}})

	def queryviadictionary(self, dictin):
		for x in dictin.keys():
			if dictin[x] != "":
				if x == "before":
					self.query["$and"].append({"year": {"$lte": int(dictin[x])}})
					
				elif x == "after":
					self.query["$and"].append({"year": {"$gte": int(dictin[x])}})
					
				else:
					self.query["$and"].append({x: {"$regex": dictin[x], "$options": "i"}})


	def execute(self):
		out = []
		result = pokedb.find(self.query)
		for x in result:
			out.append(x)
			self.query_out = out[:]      # store a copy of the array
		return out


	def pretty_print(self, limit=2147483647, order=1, count=False):
		"""Print the results of a query formatted.

		Parameters
		----------
		limit : int
			how many results to show
		order : int, -1 or 1
			Present results in forward to reverse order
		count : boolean
			Head the results with the number of total results
		"""

		if count:
			print(str(len(self.query_out)) + " results found")
		for n, x in enumerate(self.query_out[::order]):
			if n < limit:
				print(x)
