from flask import Flask, render_template, jsonify, Request, redirect, request, send_from_directory
from flask_pymongo import PyMongo
from flask_assets import Bundle, Environment
import json
import pandas as pd


app = Flask(__name__, static_folder="static", template_folder="templates")
assets = Environment(app)
app.config['FLASK_ASSETS_USE_CDN']=True

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/horses")
def horses():

    conn_horse = "mongodb+srv://dbUser:OxTrot2020@cluster0-lfpvw.azure.mongodb.net/website_db?retryWrites=true&w=majority"
    mongo_horse = PyMongo(app, uri = conn_horse)

    horse_data = list(mongo_horse.db.horses_df.find())

    horse_data_df = pd.DataFrame(horse_data)
    columns = ['Date','Horse','Jockey','Distance','FinalCall','Beyer','Odds','Starters','Trainer','FirstFracHdths','SecondFracHdths','ThirdFracHdths','FourthFracHdths','FinalTimeHdths']

    horse_data_df_mk_1 = horse_data_df[columns]
    print(horse_data_df_mk_1)
    horse_data_df_mk_1.to_csv('static/data/horses.csv')


    return render_template('horses.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route("/na_horse_rt_map")
def na_horse_rt_map():

    conn_loc = "mongodb+srv://dbUser:OxTrot2020@cluster0-lfpvw.azure.mongodb.net/location_test?retryWrites=true&w=majority"
    mongo_loc = PyMongo(app, uri = conn_loc)

    loc_data = list(mongo_loc.db.race_course_locations.find())
    loc_data_df = pd.DataFrame(loc_data)
    loc_data_df_mk_1 = loc_data_df[['lat','lon','nameLong','nameShort','url']]
    print(loc_data_df_mk_1)
    loc_data_df_mk_1.to_json('static/data/race_tracks.json', orient='records')
    
    return render_template('na_horse_rt_map.html', loc_data=loc_data)

@app.route("/op_rt")
def op_rt():

    conn_op = "mongodb+srv://dbUser:OxTrot2020@cluster0-lfpvw.azure.mongodb.net/website_db?retryWrites=true&w=majority"
    mongo_op = PyMongo(app, uri = conn_op)

    op_data = list(mongo_op.db.op_races_df.find())
    op_data_df = pd.DataFrame(op_data)
    op_data_df_mk_1 = op_data_df[['RCRace','Starters','Purse','Distance','Surface','PostTime','LongClass','Conditions']]
    print(op_data_df_mk_1)
    op_data_df_mk_1.to_csv('static/data/op_races.csv')

    return render_template('op_rt.html')

@app.route("/race_11")
def race_11():
    conn_race_11 = "mongodb+srv://dbUser:OxTrot2020@cluster0-lfpvw.azure.mongodb.net/website_db?retryWrites=true&w=majority"
    mongo_race_11 = PyMongo(app, uri = conn_race_11)
    race_11_data = list(mongo_race_11.db.race_11_df.find())
    
    columns = ['PostPosition','Horse','Trainer','Jockey','Sire','Dam','Owner','SalePrice','LastRaced','Earnings','Starts','Wins','Places','Shows','WEarnings','WStarts','WWins','WPlaces','WShows']

    race_11_data_df = pd.DataFrame(race_11_data)
    race_11_data_df_mk_1 = race_11_data_df[columns]
    print(race_11_data_df_mk_1)
    race_11_data_df_mk_1.to_csv('static/data/race_11.csv')

    return render_template('race_11.html')

if __name__ == "__main__":
    app.run(debug=True)
