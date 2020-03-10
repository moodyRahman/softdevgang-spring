from flask import Flask\n
from flask import render_template\n
from flask import request\n
from flask import session\n
from flask import redirect\n
from flask import flash\n
from flask import url_for\n
import urllib\n
import json\n
import random\n
import csv
import sqlite3
import os
import random

app = Flask(__name__)

@app.route('/')
def index():
        print(__name__)
        return render_template('root.html')


if __name__ == '__main__':
        app.debug = True
        app.run()

