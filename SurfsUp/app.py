# Import the dependencies.
import datetime as dt 
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, render_template, jsonify

#################################################
# Database Setup
#################################################

engine = create_engine ("sqlite:///../Resources/hawaii.sqlite")
Base = automap_base()

# reflect the tables
# Base.prepare(engine, reflect=True)
Base.prepare(autoload_with=engine) 
Base.classes.keys()


# Save references to each table

measurement = Base.classes.measurement
station = Base.classes.station

# reflect an existing database into a new model

# Create our session (link) from Python to the DB
# session=Session(engine)
# results = session.query(measurement, station).all()

# session.close()

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

@app.route("/")
def home():
    """List all the available api routes."""
    return (
        f"Available routes: <br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
        f"/api/v1.0/<start> <br/>"
        f"/api/v1.0/<start>/<end> <br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    results=session.query(measurement.date).all()
    session.close()

    all_dates = list(np.ravel(results))

    return jsonify(all_dates)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    results = session.query(station.station).all()
    session.close()

    all_stations = list(np.ravel(results))

    return jsonify(all_stations)

# @app.route("/api/v1.0/tobs")

# @app.route("/api/v1.0/<start>")

# @app.route("/api/v1.0/<start>/<end>")

if __name__ == '__main__':
    app.run (debug=True)



#################################################
# Flask Routes
#################################################
