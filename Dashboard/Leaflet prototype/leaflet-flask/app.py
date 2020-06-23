from flask import Flask, render_template, jsonify, Request, redirect, request, send_from_directory
from flask_pymongo import PyMongo
from flask_assets import Bundle, Environment
import json
import pandas as pd


app = Flask(__name__, static_folder="static")
assets = Environment(app)
app.config['FLASK_ASSETS_USE_CDN']=True

# js = Bundle('config.js', 'logic.js', output='static/js/main.js')
# assets.register('main_js', js)

conn = "mongodb+srv://dbUser:OxTrot2020@cluster0-lfpvw.azure.mongodb.net/location_test?retryWrites=true&w=majority"
mongo = PyMongo(app, uri = conn)

@app.route("/")
def index():
    loc_data = list(mongo.db.race_course_locations.find())
    # print(loc_data)
    loc_data_df = pd.DataFrame(loc_data)
    loc_data_df_mk_1 = loc_data_df[['lat','lon','nameLong','nameShort','url']]
    print(loc_data_df_mk_1)
    loc_data_df_mk_1.to_json('static/js/race_tracks.json', orient='records')
    return render_template("index.html", loc_data=loc_data)


if __name__ == "__main__":
    app.run(debug=True)
