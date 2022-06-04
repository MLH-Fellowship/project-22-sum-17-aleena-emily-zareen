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
    authorFirstName = "Aleena"
    authorLastName = "Tim"
    workExperience = [{'title': 'WiTNY Robotics Researcher', 'company': 'WiTNY Research Foundation', 'startDate': 'Sep 2018', 'endDate': 'Dec 2018'},
                      {'title': 'Coding Instructor', 'company': 'ScholarStem', 'startDate': 'Sep 2021', 'endDate': 'May 2022'},
                      {'title': 'WiTNY Robotics Researcher', 'company': 'WiTNY Research Foundation', 'startDate': 'Sep 2018', 'endDate': 'Dec 2018'}]
    return render_template('aleena-portfolio.html', title="Aleena's Portfolio", url=os.getenv("URL"), authorFirstName="Aleena", authorLastName="Tim", workExperience=workExperience)
@app.route('/emily-portfolio')
def emily_portfolio_page():
    return render_template('emily-portfolio.html', title="Emily's Portfolio", url=os.getenv("URL"), author="Emily")
@app.route('/zareen-portfolio')
def zareen_portfolio_page():
    return render_template('zareen-portfolio.html', title="Zaneer's Portfolio", url=os.getenv("URL"), author="Zareen")
