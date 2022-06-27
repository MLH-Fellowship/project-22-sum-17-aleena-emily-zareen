from peewee import *
from flask import Flask, render_template, json, url_for, request, redirect
from app.map_app import map_app
import folium
import os
import json
import datetime
from dotenv import load_dotenv
from playhouse.shortcuts import model_to_dict
from pathlib import Path
load_dotenv('.env')
app = Flask(__name__)

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"), user=os.getenv("MYSQL_USER"),
                     password=os.getenv("MYSQL_PASSWORD"), host="178.128.229.22", port=3306)

print(mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

app.register_blueprint(map_app)
dataFile = open(Path("app\static\data.json") , encoding = "utf-8")

data = json.load(dataFile)

@app.route('/')
def index():    
    allUsers = data    
    return render_template('index.html', title="Home", allUsers=allUsers)

@app.route('/aleena-tim-portfolio')
def aleena_portfolio():
    allUsers = data    
    return render_template('aleena-tim-portfolio.html', allUsers=allUsers)

@app.route('/emily-lai-portfolio')
def emily_portfolio():
    allUsers = data    
    return render_template('emily-lai-portfolio.html', allUsers=allUsers)

@app.route('/zareen-kabir-portfolio')
def zareen_portfolio():
    allUsers = data    
    return render_template('zareen-kabir-portfolio.html', allUsers=allUsers)

@app.route('/hobbies')
def hobbies():    
    return render_template('hobbies.html')

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in
TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }
 
if __name__ == "__main__":
    app.run(debug=True)

