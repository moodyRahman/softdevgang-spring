# Moody Rahman, Sophie Nichol, Jude Rizzo
# SoftDev pd 9
# K10 -- Import/Export Bank
# 2020-02-29
'''
    name of dataset and description of its contents
    hyperlink to where raw data is hosted
    brief summary of your import mechanism
    
    movies scraped from wikipedia
    https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json
    
    
    import mechanism
    
    this is done with code that is garunteed to run as either an import or when directly executed
    it establishes a connection to mongod and switches to the "movies" collection in the "test" db
    it then counts how many documents there are in "movies" and if it's zero, parse the movies.json and insert each element
    if there are documents inside "movies" then it will do nothing
    

    the query object was meant to facillitate query's with multiple parameters 
    multiple query calls can be formatted as 
    q = Query() 
    q.actor("mood").afteryear(2002)
    --or--
    q = Query()
    q.actor("mood")
    q.afteryear(2002)

'''



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
        super(Query, self).__init__()
        self.query = {"$and":[]}
        self.query_out = []

    
    def genre(self, gen):

        """Specify a genre to search the database by

        Parameters
        ----------
        gen : String
            Name of genre to query by

        Returns
        -------
        Query
            this instance of Query

        """

        self.query["$and"].append({"genres":{"$regex":gen, "$options": "i"}})
        return self


    def title(self, name):

        """Specify a title to search the database by

        Parameters
        ----------
        name : type
            Name of movie to query for.

        Returns
        -------
        Query
            this instance of Query.

        """

        self.query["$and"].append({"title":{"$regex":name, "$options": "i"}})
        return self


    def actor(self, name):

        """Specify an actor to search the database by

        Parameters
        ----------
        name : String
            name of actor to query for.

        Returns
        -------
        Query
            this instance of Query

        """

        self.query["$and"].append({"cast":{"$regex":name, "$options": "i"}})
        return self


    def beforeyear(self, before):
        
        """Specify what year after to search the database by

        Parameters
        ----------
        before : int
            Which year the query should search before

        Returns
        -------
        Query
            this instance of Query

        """
        
        self.query["$and"].append({"year":{"$lte":before}})
        return self


    def afteryear(self, after):
        
        """Specify what year after to search the database by.

        Parameters
        ----------
        after : int
            What year should the query search after

        Returns
        -------
        Query
            this instance of Query

        """
        
        self.query["$and"].append({"year":{"$gte":after}})
        return self


    def execute(self):
        
        """Execute the query and set query_out to the results

        Returns
        -------
        list
            list containing a deep copy of query_out

        """
        
        out = []
        result = collection.find(self.query)
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

