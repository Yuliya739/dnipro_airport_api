from datetime import datetime, timedelta
from models.models import Airline, Flight
from flask import jsonify
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask import Flask
from sqlalchemy.sql.schema import MetaData

# __init__
engine = create_engine('postgresql+psycopg2://postgres:kaktys33@localhost/dneprairport')
connection = engine.connect()
metadata = MetaData()

app = Flask(__name__, instance_relative_config = True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:kaktys33@localhost/dneprairport'
db = SQLAlchemy(app)

db.create_all()
#/__init__

def model_to_json(data):
    return jsonify([value.to_dict() for value in data])

def flights_today(is_departure: bool):
    current_time = datetime.now()
    final_time = current_time + timedelta(days=1)  ;
    data = db.session.query(Flight).filter(Flight.estimated_time.between(current_time,final_time), Flight.is_departure == is_departure).all()
    return model_to_json(data), 200

@app.route('/arrival/today', methods=['GET'])
def arrivals_today():
    if request.method == 'GET':
        return flights_today(False)

@app.route('/departure/today', methods=['GET'])
def departures_today():
    if request.method == 'GET':
        return flights_today(True)

@app.route('/flight', methods = ['POST', 'GET'])
def add_flight():
    if request.method == 'POST':
        body = request.get_json(True)
        flight = Flight(body['is_departure'], body['estimated_time'], body['direction'],\
            body['real_time'], body['terminal'], body['airline_id'], body['gate'], body['remark'],\
                body['airport_name'])
        db.session.add(flight)
        db.session.commit()
        return 'Done', 200
    if request.method == 'GET':
        data = db.session.query(Flight).all()
        return model_to_json(data), 200

@app.route('/airline', methods=['GET', 'POST'])
def airline():
    if request.method == 'GET':
        data = db.session.query(Airline).all()
        return model_to_json(data), 200
    if request.method == 'POST':
        body = request.get_json(True)
        airline = Airline(body['airline_name'], body['country'], body['iso31661_alpha2'],\
            body['iso31661_alpha3'], body['iata'], body['icao'],\
                body['carriage_class'], body['call_center'])
        db.session.add(airline)
        db.session.commit()
        return 'Done', 200