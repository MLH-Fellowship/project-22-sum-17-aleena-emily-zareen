from flask import Flask, render_template, request, json,  url_for, request, redirect
from app.map_app import map_app
import folium
import os
import json
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
app.register_blueprint(map_app)
dataFile = open("app\static\data.json" , encoding = "mbcs")

data = json.load(dataFile)

@app.route('/')
def index():    
    allUsers = data    
    return render_template('index.html', title="Homepage", allUsers=allUsers)

@app.route('/aleena-tim-portfolio')
def aleena_portfolio():
    allUsers = data    
    return render_template('aleena-tim-portfolio.html', title="Aleena", allUsers=allUsers)

@app.route('/emily-lai-portfolio')
def emily_portfolio():
    allUsers = data    
    return render_template('emily-lai-portfolio.html', title="Emily", allUsers=allUsers)

@app.route('/zareen-kabir-portfolio')
def zareen_portfolio():
    allUsers = data    
    return render_template('zareen-kabir-portfolio.html', title="Zareen", allUsers=allUsers)
 
if __name__ == "__main__":
    app.run(debug=True)