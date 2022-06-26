<<<<<<< Updated upstream
from flask import Flask, render_template, request, json,  url_for, request, redirect
from app.map_app import map_app
import folium
import os
import json
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)

mydb =
MySQLDatabase(os.getenv("MYSQL_DATABASE"),
              user=os.getenv("MYSQL_USER"),
              password=os.getenv("MYSQL_PASSWORD"),
              host=os.getenv("MYSQL_HOST"),
              port=3306
             )

print(db)

app.register_blueprint(map_app)
dataFile = open("app\static\data.json" , encoding = "utf-8")

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
 
if __name__ == "__main__":
    app.run(debug=True)
=======
from flask import Flask, render_template, request, json,  url_for, request, redirect
from app.map_app import map_app
import folium
import os
import json
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
app.register_blueprint(map_app)
dataFile = open("C:/Users/8300us2/Desktop/MLH Fellowship/Flask portfolio/project-22-sum-17-aleena-emily-zareen/app/static/data.json" , encoding = "mbcs")

data = json.load(dataFile)

@app.route('/')
def index():    
    allUsers = data    
    return render_template('index.html', title="Home", allUsers=allUsers)

@app.route('/aleena-tim-portfolio')
def aleena_portfolio():
    allUsers = data    
    return render_template('aleena-tim-portfolio.html', title="Aleena", allUsers=allUsers)

@app.route('/portfolio/emily-portfolio')
def emily_portfolio():
    allUsers = data    
    return render_template('emily-portfolio.html', title="Emily", allUsers=allUsers)

@app.route('/portfolio/zareen-portfolio')
def zareen_portfolio():
    allUsers = data    
    return render_template('zareen-portfolio.html', title="Zareen", allUsers=allUsers)

#@app.route('/emily-portfolio')
#def emily_portfolio_page():
#    return render_template('emily-portfolio.html', title="Emily's Portfolio", url=os.getenv("URL"), author="Emily")

#@app.route('/zareen-portfolio')
#def zareen_portfolio_page():
#    return render_template('zareen-portfolio.html', title="Zareen's Portfolio", url=os.getenv("URL"), author="Zareen")
    
if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> Stashed changes
