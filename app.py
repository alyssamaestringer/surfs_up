# Add imports
import datetime as dt
import numpy as np
import pandas as pd

#Imports from sqlalchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Set up database
engine = create_engine("sqlite:///hawaii.sqlite")

#Reflect the database into our classes
Base = automap_base()

#reflect the database
Base.prepare(engine, reflect=True)

#Save refrences to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#Create session link
session = Session(engine)

# Create a new Flask app instance, instance is refering to a singular version of something
app = Flask(__name__)

#Creating our first route or starting point otherwise known as root
#forward slash denotes that we want to put our data at the root of our routes
#When creating routes, we follow the naming convention /api/v1.0/ followed by the name of the route. 
@app.route('/')
def welcome():
    return(
        '''
        Welcome to the Climate Analysis API!
        Available Routes:
        /api/v1.0/precipitation
        /api/v1.0/stations
        /api/v1.0/tobs
        /api/v1.0/temp/start/end
        ''')

#Create a route for percipitation
@app.route("/api/v1.0/precipitation")
def percipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

#Create a route for stations
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

#Create route for tobs
#list(np.ravel) is how you unravel the results into a one-dimensional array and convert that array into a list. 
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

#Create a route with minimum, avg and max temps
#we have to provide both a starting and ending date
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)