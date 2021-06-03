from datetime import datetime, timedelta
from sqlalchemy.sql.functions import current_date

from sqlalchemy.sql.sqltypes import DateTime
from models.models import Admin, Flight
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


@app.route('/admin', methods=['POST', 'GET'])
def admins():
    if request.method == 'GET':
        data = db.session.query(Admin).all()
        return jsonify([value.to_dict() for value in data]), 200
    if request.method == 'POST':
        db.session.add(Admin(**request.get_json(True)))
        db.session.commit()
        return 'Done', 200

@app.route('/admin/auth', methods = ['POST'])
def auth():
    if request.method == 'POST':
        data = db.session.query(Admin).filter(Admin.admin_id == request.get_json(True)['admin_id'] and\
            Admin.password == request.get_json(True)['password']).first()
        if data:
            return 'Done', 200
        else:
            return 'Error', 404

@app.route('/departures/today', methods=['GET'])
def departures_today():
    if request.method == 'GET':
        current_time = datetime.now()
        final_time = current_time + timedelta(days=1)  ;
        data = db.session.query(Flight).filter(Flight.estimated_time.between(current_time,final_time), Flight.is_departure == True).all()
        return jsonify([value.to_dict() for value in data]), 200
