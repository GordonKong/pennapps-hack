import urllib.request
from flask import Flask, render_template, redirect, url_for, request, flash, jsonify
import json
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'pennapps'
app.config['MONGO_URI'] = 'mongodb+srv://pennapps:.@cluster0.cpkso.mongodb.net/pennapps?retryWrites=true&w=majority'

mongo = PyMongo(app)
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    value = None
    with open("itemList.json", "r") as itemListFile:    
        itemList = json.load(itemListFile)
    if request.method == "POST":
        value = request.form.get('product')
        return render_template('index.html', itemList=itemList, value=value)
    return render_template('index.html', itemList=itemList)

@app.route("/about")
def about():
    return render_template("about.html")
        



