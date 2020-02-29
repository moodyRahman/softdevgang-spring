import mongo 
from mongo import Query






q = Query()

q.actor("michael")
q.execute()

q.pretty_print(limit=10)