import urllib.request
from flask import Flask, render_template, redirect, url_for, request, flash
import json
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
        



