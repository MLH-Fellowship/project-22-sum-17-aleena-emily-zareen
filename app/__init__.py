from flask import Flask, render_template, request, json,  url_for, request, redirect
from app.map_app import map_app
import folium
import os
import json
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
app.register_blueprint(map_app)
dataFile = open("C:/Users/aleen/Desktop/project-22-sum-17-aleena-emily-zareen/app/static/data.json" , encoding = "mbcs")

data = json.load(dataFile)

@app.route('/')
def index():    
    allUsers = data    
    return render_template('index.html', title="Home", allUsers=allUsers)

@app.route('/portfolio/<string:username>')
def portfolio(username):
    userData = data[username]
    allUsers = data
    return render_template('portfolio.html', username=username, userData=userData, allUsers=allUsers)

@app.route('/portfolio')
def b_portfolio():
    return render_template('portfolio.html')

#@app.route('/emily-portfolio')
#def emily_portfolio_page():
#    return render_template('emily-portfolio.html', title="Emily's Portfolio", url=os.getenv("URL"), author="Emily")

#@app.route('/zareen-portfolio')
#def zareen_portfolio_page():
#    return render_template('zareen-portfolio.html', title="Zareen's Portfolio", url=os.getenv("URL"), author="Zareen")
    
if __name__ == "__main__":
    app.run(debug=True)