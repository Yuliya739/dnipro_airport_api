from flask import Flask
# import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask import jsonify
import sqlalchemy
from sqlalchemy.sql.schema import MetaData, Table
from sqlalchemy.sql.sqltypes import String
from sqlalchemy_serializer import SerializerMixin
import uuid

from werkzeug.wrappers import response

engine = create_engine('postgresql+psycopg2://postgres:kaktys33@localhost/dneprairport')
connection = engine.connect()
metadata = MetaData()
admin = Table('admin', metadata, autoload = True, autoload_with = engine)

app = Flask(__name__, instance_relative_config = True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:kaktys33@localhost/dneprairport'
db = SQLAlchemy(app)

class CustomSerializerMixin(SerializerMixin):
    serialize_types = (
        (uuid.UUID, lambda x: str(x)),
    )

class admin(db.Model, CustomSerializerMixin):

   serialize_only = ('admin_id', 'last_name', 'first_name', 'patronymic', 'password')

   admin_id = db.Column('admin_id', db.String(100), primary_key = True)
   last_name = db.Column(db.String(100))
   first_name = db.Column(db.String(100))  
   patronymic = db.Column(db.String(100))
   password = db.Column(db.String(20))

def __init__(self, last_name, first_name, patronymic, password):
   self.last_name = last_name
   self.first_name = first_name
   self.patronymic = patronymic
   self.password = password

db.create_all()

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/admin/keys')
def admin_keys():
    return jsonify(admin.columns.keys())

@app.route('/admin')
def admins():
    data = admin.query.all()
    return jsonify(list(map(lambda value: value.to_dict(), data)))

@app.route('/insertdata')
def insertdata():
    #.....
    sql_row = sqlalchemy.text("""INSERT INTO admin(admin_id, last_name, first_name, patronymic, password)
     VALUES (:admin_id, :last_name, :first_name, :patronymic, :password)""")
    data = {"admin_id": "003", "last_name": "Kycheryagin", "first_name": "Vasiliy", "patronymic": "Ivanovich", "password": "qwerty456"}
    connection.execute(sql_row, data)

    return "ok"