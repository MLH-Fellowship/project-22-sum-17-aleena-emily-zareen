import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="Portfolio Home", url=os.getenv("URL"))
@app.route('/base-portfolio')
def portfolio_page():
    return render_template('base-portfolio.html', title="Aleena's Portfolio", url=os.getenv("URL"), author="Aleena")
"""@app.route('/emily-portfolio')
def index():
    return render_template('index.html', title="Emily's Portfolio", url=os.getenv("URL"), author="Emily")
@app.route('/zareen-portfolio')
def index():
    return render_template('index.html', title="Zaneer's Portfolio", url=os.getenv("URL"), author="Zareen")
"""