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

# session.close()

#################################################
# Flask Setup
#################################################

app = Flask(__name__)



#################################################
# Flask Routes
#################################################

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
    results=session.query(measurement.date, func.avg(measurement.prcp)) \
.filter(measurement.date <= '2017-08-23') \
.filter(measurement.date >= '2016-08-23') \
.group_by(func.strftime('%m', measurement.date)) \
.all()
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

@app.route("/api/v1.0/tobs")
def temperatures():
    session = Session(engine)
    results = session.query(measurement.date, measurement.tobs) \
.filter(measurement.station == 'USC00519281')\
.filter(measurement.date <= '2017-08-23') \
.filter(measurement.date >= '2016-08-23') \
.order_by(func.strftime('%m', measurement.date)) \
.all()
    session.close()

    all_temps = list(np.ravel(results))

    return jsonify(all_temps)

@app.route("/api/v1.0/<start>")
def start():
    session = Session(engine)
    results = session.query(measurement.date, func.max(measurement.tobs), func.min(measurement.tobs), func.avg(measurement.tobs)) \
.filter(measurement.station == 'USC00519281')\
.filter(measurement.date >= '2016-08-23') \
.all()
    session.close()
    
    start_date = list(np.ravel(results))

    return jsonify(start_date)

@app.route("/api/v1.0/<start>/<end>")
def start():
    session = Session(engine)
    results = session.query(measurement.date, func.max(measurement.tobs), func.min(measurement.tobs), func.avg(measurement.tobs)) \
.filter(measurement.station == 'USC00519281')\
.filter(measurement.date <= '2017-08-23') \
.filter(measurement.date >='2016-08-23')\
.all()
    session.close()
    
    end_date = list(np.ravel(results))

    return jsonify(end_date)

if __name__ == '__main__':
    app.run (debug=True)



