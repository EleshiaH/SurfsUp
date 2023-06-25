# Import the dependencies.
import datetime as dt 
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

engine = create_engine ("sqlite:///../Resources/hawaii.sqlite", echo=False)

Base = automap_base()
Base.prepare(autoload_with=engine)
Base.classes.keys()

['station',
 'date',
 'prcp',
 'tobs']


    

# reflect an existing database into a new model

# reflect the tables


# Save references to each table


# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################

app = Flask(__name__)

@app.route("/")
def home():
    print ("welcome to home")
    return "Welcome to home"

if __name__ == '__main__':
    app.run (debug=True)
    


#################################################
# Flask Routes
#################################################
