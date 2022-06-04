import os
from flask import Flask, render_template, request
from app.map_app import map_app
import folium
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)

app.register_blueprint(map_app)

@app.route('/')
def index():
    return render_template('index.html', title="Portfolio Home", url=os.getenv("URL"))
@app.route('/aleena-portfolio')
def aleena_portfolio_page():
    return render_template('aleena-portfolio.html', title="Aleena's Portfolio", url=os.getenv("URL"), author="Aleena")
@app.route('/zareen-portfolio')
def zareen_portfolio_page():
    return render_template('zareen-portfolio.html', title="Zareen's Portfolio", url=os.getenv("URL"), author="Zareen")

"""@app.route('/emily-portfolio')
def index():
    return render_template('index.html', title="Emily's Portfolio", url=os.getenv("URL"), author="Emily")
@app.route('/zareen-portfolio')
def index():
    return render_template('index.html', title="Zaneer's Portfolio", url=os.getenv("URL"), author="Zareen")
"""