from flask import Flask, render_template, Request, redirect, request, send_from_directory
from flask_pymongo import PyMongo
from flask_assets import Bundle, Environment
import os


app = Flask(__name__, static_folder="static")
assets = Environment(app)
app.config['FLASK_ASSETS_USE_CDN']=True

# js = Bundle('config.js', 'logic.js', output='static/js/main.js')
# assets.register('main_js', js)

conn = "mongodb+srv://dbUser:OxTrot2020@cluster0-lfpvw.azure.mongodb.net/location_test?retryWrites=true&w=majority"
mongo = PyMongo(app, uri = conn)
 
@app.route("/")
def index():
    loc_data = mongo.db.race_course_locations.find_one()
    print(loc_data)
    return render_template("index.html", loc_data=loc_data)


if __name__ == "__main__":
    app.run(debug=True)
