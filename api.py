from datetime import datetime, timedelta
from models.models import Airline, Flight, Orders, Plane, Ticket, Transplantation
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask import Flask
from sqlalchemy.sql.schema import MetaData
from sqlalchemy import func
from werkzeug.datastructures import Headers
from flask import request, Response
import dateutil.parser

# __init__
engine = create_engine('postgresql+psycopg2://postgres:kaktys33@localhost/dneprairport')
connection = engine.connect()
metadata = MetaData()

app = Flask(__name__, instance_relative_config = True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:kaktys33@localhost/dneprairport'
db = SQLAlchemy(app)

db.create_all()

cors_headers = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "*",
    "Access-Control-Allow-Credentials": "true",
    "Access-Control-Allow-Methods": "*",
    "Access-Control-Expose-Headers": "Link,X-Total,X-Per-Page,X-RateLimit-Limit,X-RateLimit-Remaining",
    "Vary": "Accept-Encoding, Origin,Authorization,client-geo-region"
}
@app.after_request
def after_request(response: Response):
    headers = dict(response.headers)
    headers["Cache-Control"] = "no-transform"
    headers.update(**cors_headers)
    response.headers = Headers(headers)
    return response

@app.before_request 
def before_request():
    if request.method == 'OPTIONS':
        return None, 200, cors_headers
#/__init__

def models_to_list_json(data):
    return jsonify([value.to_dict() for value in data])

def flights_today(is_departure: bool):
    current_time = datetime.now()
    final_time = current_time + timedelta(days=1)
    data = db.session.query(Flight).filter(Flight.estimated_time.between(current_time,final_time), Flight.is_departure == is_departure).all()
    return models_to_list_json(data), 200, {'Content-Type': 'application/json'}

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
        body = request.form
        flight = Flight(body['is_departure'] == 'true', body['estimated_time'], body['direction'],\
            body['terminal'], body['plane_id'], body['gate'],\
                 body['travel_time'], body['remark'],\
                body['airport_name'], body['coast'], body.get('real_time'))
        db.session.add(flight)
        ticket_count = db.session.query(Plane).filter(Plane.plane_id == body['plane_id']).first().kol_seats
        for i in range(ticket_count):
            db.session.add(Ticket(flight.flight_id))
        db.session.commit()
        return flight.flight_id, 200
    if request.method == 'GET':
        data = db.session.query(Flight).all()
        return models_to_list_json(data), 200

@app.route('/trans', methods=['POST', 'GET'])
def add_trans():
    if request.method == 'POST':
        parser = request.form
        time = parser['time']
        gate = parser['gate']
        transfer = parser['company_transfer']
        flight_id = parser['flight_id']
        trans = Transplantation(time, gate, transfer, flight_id)
        db.session.add(trans)
        db.session.commit()
        return trans.transplantation_id, 200
    if request.method == 'GET':
        id = request.args.get('flight_id')
        trans = db.session.query(Transplantation).filter(Transplantation.flight_id == id).first()
        if trans:
            return jsonify(trans.to_dict()), 200
        else:
            return 'Not found', 201

@app.route('/airline', methods=['GET', 'POST'])
def airline():
    if request.method == 'GET':
        plane_id = request.args.get('plane_id')
        if plane_id:
            plane = db.session.query(Plane).filter(Plane.plane_id == plane_id).first()
            airline = db.session.query(Airline).filter(Airline.airline_id == plane.airline_id).first()
            return jsonify(airline.to_dict()), 200
        else:
            data = db.session.query(Airline).all()
            return models_to_list_json(data), 200
    if request.method == 'POST':
        body = request.form
        airline = Airline(body['airline_name'], body['country'], body['iso31661_alpha2'],\
            body['iso31661_alpha3'], body['iata'], body['icao'],\
                body['carriage_class'], body['call_center'])
        db.session.add(airline)
        db.session.commit()
        return airline.airline_id, 200

@app.route('/flight/search', methods=['GET'])
def search_flight():
    date = dateutil.parser.parse(request.args.get('date'))
    start = date.date();
    end = start + timedelta(days=1)
    destination = request.args.get('destination')
    data =  db.session.query(Flight).\
            filter(func.lower(Flight.direction).contains(func.lower(destination))).\
            filter(Flight.estimated_time.between(start, end)).\
            filter(Flight.is_departure == True)
    # data = db.session.query(Flight).outerjoin(Transplantation,  Flight.flight_id == Transplantation.flight_id).\
    #     filter(Flight.direction.contains(destination)).\
    #     filter(Flight.estimated_time.between(start, end))

    return models_to_list_json(data), 200

@app.route('/plane', methods=['GET', 'POST'])
def plane():
    if request.method == 'GET':
        airline_id = request.args.get('airline_id')
        if airline_id:
            data = db.session.query(Plane).filter(Plane.airline_id == airline_id).all()
            return models_to_list_json(data), 200
        else:
            data = db.session.query(Plane).all()
            return models_to_list_json(data), 200
    if request.method == 'POST':
        body = request.form
        plane = Plane(body['plane_name'], body['kol_seats'], body['airline_id'])
        db.session.add(plane)
        db.session.commit()
        return plane.plane_id, 200

@app.route('/ticket', methods=['GET'])
def ticket():
    if request.method == 'GET':
        flight_id = request.args.get('flight_id')
        data = db.session.query(Ticket).filter(Ticket.flight_id == flight_id).all()
        return models_to_list_json(data), 200

@app.route('/orders', methods=['POST'])
def orders():
    if request.method == 'POST':
        body = request.form
        order = Orders(body['last_name'], body['first_name'], body['date_of_birthday'],\
             body['num_passport'], body['valid_until'], body['email'])
        db.session.add(order)
        flight_id = body.get('flight_id')
        ticket = db.session.query(Ticket).filter(Ticket.order_id == None).filter(Ticket.flight_id == flight_id).first()
        ticket.order_id = order.order_id
        db.session.merge(ticket)
        db.session.commit()
        return order.order_id, 200
