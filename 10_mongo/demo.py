import mango 
from mango import Query






q = Query()

q.actor("michael").genre("drama")

q.execute()


q.pretty_print(limit=5, order=1, count=True)