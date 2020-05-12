from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo


app = Flask(__name__)

db_link = "mongodb+srv://dbUser:OxTrot2020@cluster0-lfpvw.azure.mongodb.net/test?retryWrites=true&w=majority"
mongo =PyMongo(app, uri = db_link) 

@app.route("/")
def index():
    return 

if __name__ == "__main__":
    app.run(debug=True)

