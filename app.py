#!/usr/bin/python

from flask import Flask, request,url_for
from flask_restful import Resource, Api
from requests import put, get
from json import dumps
from resources.helper import get_dictionary, find_ngrams, find_matches
import re
app = Flask(__name__)
api = Api(app)

todos = {}

class message_Conversion(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        
        data = request.form['data']
        words = find_ngrams(data.split(), len(data.split()))
        matches = find_matches(words,get_dictionary())
        todos[todo_id] = matches
        
        return {todo_id: matches}

api.add_resource(message_Conversion, '/<string:todo_id>')

if __name__ == '__main__':
    app.run()