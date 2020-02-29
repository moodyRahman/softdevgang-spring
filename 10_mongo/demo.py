import mongo 
from mongo import Query






q = Query()

q.actor("michael").genre("drama")

q.execute()


q.pretty_print(limit=10)