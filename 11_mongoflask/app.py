from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import flash
from flask import url_for
import urllib
import json
import random
import csv
import sqlite3
import os
import random
import moviemango
import pokemango
from moviemango import MovieQuery
from pokemango import PokeQuery

app = Flask(__name__)

@app.route('/')
def index():
        print(__name__)
        return render_template('root.html')

@app.route('/movie')
def movie_parse():
        query = MovieQuery()
        query.queryviadictionary(request.args)
        print(query.query)
        result = query.execute()
        return render_template("movie.html", results = result)

@app.route('/poke')
def poke_parse():
        query = PokeQuery()
        query.queryviadictionary(request.args)
        result = query.execute()
        return render_template("poke.html", results = result)



if __name__ == '__main__':
        app.debug = True
        app.run()

