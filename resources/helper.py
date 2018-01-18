#!/usr/bin/python

from flask import Flask, request,url_for
from flask_restful import Resource, Api
from requests import put, get
from json import dumps
import re

def get_dictionary():
    words=[]
    filename = "resources/phrases"
    file = open(filename, "r")
    for line in file:
        line = re.sub(r'\n', '', line)
        words.append(line) 
    return words

def find_ngrams(input_list, n):
    n_grams = []
    n_grams_joined=[]
    for k in range(n):
        n_gram = list(zip(*[input_list[i:] for i in range(k+1)]))
        n_grams.append(n_gram)
        
    for i in range(len(n_grams)):
        for k in range(len(n_grams[i])):
            #print (' '.join(x[i][k]))
            n_grams_joined.append(' '.join(n_grams[i][k]))
            
    return n_grams_joined

def find_matches(words,library):
    matches = []
    if not words or not library:
        matches.append("No words or Library found")
    else:
        matches = [x for x in words if x in library]
    return matches