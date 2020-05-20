from flask import Flask, render_template, jsonify, Request, redirect, request, send_from_directory
from flask_pymongo import PyMongo
from flask_assets import Bundle, Environment
import json
import pandas as pd


app = Flask(__name__, static_folder="static")
assets = Environment(app)
app.config['FLASK_ASSETS_USE_CDN']=True

@app.route("/")
def index():
    number = 1
    return render_template('index.html', number=number)

@app.route("/horses")
def horses():
    return render_template('horses.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route("/templates/na_horse_rt_map")
def na_horse_rt_map():
    return render_template('na_horse_rt_map.html')

@app.route("/op_rt")
def op_rt():
    return render_template('op_rt.html')

@app.route("/race_11")
def race_11():
    return render_template('race_11.html')

if __name__ == "__main__":
    app.run(debug=True)
