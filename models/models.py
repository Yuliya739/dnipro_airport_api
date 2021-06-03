import uuid
from sqlalchemy import Column, String, SmallInteger, Boolean, CheckConstraint, ForeignKey, DateTime, Index
from sqlalchemy.sql.sqltypes import Date, Integer
from models.custom_serializer import CustomSerializerMixin
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Admin(Base, CustomSerializerMixin):
   __tablename__ = 'admin'

   admin_id = Column(String(), primary_key = True, nullable=False, name = 'admin_id', default=lambda: str(uuid.uuid4()))
   last_name = Column(String(), nullable=False)
   first_name = Column(String(), nullable=False)  
   patronymic = Column(String(), nullable=False)
   password = Column(String(), nullable=False)

   def __init__(self, last_name, first_name, patronymic, password, admin_id = None):     
        if admin_id: 
            self.admin_id = admin_id
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.password = password       

class Plane(Base, CustomSerializerMixin):
    __tablename__ = 'plane'

    plane_id = Column(String(), nullable=False, primary_key = True, name = 'plane_id', default=lambda: str(uuid.uuid4()))
    plane_name = Column(String(), nullable=False)
    kol_seats = Column(String(), nullable=False) 

    def __init__(self, plane_name, kol_seats, plane_id = None):
        if plane_id:
            self.plane_id = plane_id
        self.plane_name = plane_name
        self.kol_seats = kol_seats

class Orders(Base, CustomSerializerMixin):
    __tablename__ = 'orders'

    order_id = Column(String(100), nullable=False, primary_key = True, name = 'order_id',  default=lambda: str(uuid.uuid4()))
    last_name = Column(String(100), nullable=False)
    first_name = Column(String(100), nullable=False)
    date_of_birthday = Column(Date(), nullable=False)
    num_passport = Column(Integer(), nullable=False)
    valid_until = Column(Date(), nullable=False)
    email = Column(String(100), nullable=False) 

    def __init__(self, last_name, first_name, date_of_birthday, num_passport, valid_until, email,  order_id = None):
        if order_id:
            self.order_id = order_id
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birthday = date_of_birthday
        self.num_passport = num_passport
        self.valid_until = valid_until
        self.email = email

class Transplantation(Base, CustomSerializerMixin):
    __tablename__ = 'transplantation'

    transplantation_id = Column(String(), nullable=False, primary_key = True, name = 'transplantation_id',  default=lambda: str(uuid.uuid4()))
    transplantation_date = Column(DateTime(), nullable=False)
    gate = Column(String(), nullable=False)
    company_transfer = Column(String(), nullable=False)

    def __init__(self, transplantation_date, gate, company_transfer, transplantation_id = None):
        if transplantation_id:
            self.transplantation_id = transplantation_id
        self.transplantation_date = transplantation_date
        self.gate = gate        
        self.company_transfer = company_transfer

class ArivalFlight(Base, CustomSerializerMixin):
    __tablename__ = 'arrival_flight'

    arrival_id = Column(String(), nullable=False, primary_key = True, name = 'arrival_id',  default=lambda: str(uuid.uuid4()))
    direction = Column(String(), nullable=False)
    arrival_date = Column(DateTime(), nullable=False)
    terminal = Column(String(), nullable=False)
    gate = Column(String(), nullable=False)
    remark = Column(String(), nullable=False)
    airport_name = Column(String(), nullable=False)

    def __init__(self, direction, arrival_date, terminal, gate, remark, airport_name, arrival_id = None):
        if arrival_id:
            self.arrival_id = arrival_id
        self.direction = direction
        self.arrival_date = arrival_date        
        self.terminal = terminal
        self.gate = gate
        self.remark = remark        
        self.airport_name = airport_name

class DepartureFlight(Base, CustomSerializerMixin):
    __tablename__ = 'departure_flight'

    departure_id = Column(String(), nullable=False, primary_key = True, name = 'departure_id',  default=lambda: str(uuid.uuid4()))
    real_time = Column(DateTime(), nullable=False)
    terminal = Column(String(), nullable=False)
    gate = Column(String(), nullable=False)
    remark = Column(String(), nullable=False)
    airport_name = Column(String(), nullable=False)

    def __init__(self, arrival_date, terminal, gate, remark, airport_name, departure_id = None):
        if departure_id:
            self.departure_id = departure_id
        self.arrival_date = arrival_date        
        self.terminal = terminal
        self.gate = gate
        self.remark = remark        
        self.airport_name = airport_name

class Flight(Base, CustomSerializerMixin):
    __tablename__ = 'flight'

    flight_id = Column(String(), nullable=False, primary_key = True, name = 'flight_id',  default=lambda: str(uuid.uuid4()))
    direction = Column(String(), nullable=False)
    departure_date = Column(DateTime(), nullable=False)
    airline_name = Column(String(), nullable=False)
    arrival_id = Column(String(), ForeignKey('arrival_flight.arrival_id', ondelete='CASCADE'), nullable=False, unique=True)
    departure_id = Column(String(), ForeignKey('departure_flight.departure_id', ondelete='CASCADE'), nullable=False, unique=True)
    transplantation_id = Column(String(), ForeignKey('transplantation.transplantation_id', ondelete='CASCADE'), nullable=False)

    def __init__(self, direction, departure_date, airline_name, arrival_id, departure_id, transplantation_id, flight_id = None):
        if flight_id:
            self.flight_id = flight_id
        self.direction = direction        
        self.departure_date = departure_date
        self.airline_name = airline_name
        self.arrival_id = arrival_id        
        self.departure_id = departure_id        
        self.transplantation_id = transplantation_id

class Tiket(Base, CustomSerializerMixin):
    __tablename__ = 'ticket'

    ticket_id = Column(String(), nullable=False, primary_key = True, name = 'ticket_id', default=lambda: str(uuid.uuid4()))
    air_ticket_class = Column(String(), nullable=False)
    order_id = Column(String(), ForeignKey('orders.order_id', ondelete='CASCADE'))
    flight_id = Column(String(), ForeignKey('flight.flight_id', ondelete='CASCADE'), nullable=False)

    def __init__(self, air_ticket_class, order_id, flight_id, ticket_id = None):
        if ticket_id:
            self.ticket_id = ticket_id
        self.air_ticket_class = air_ticket_class
        self.order_id = order_id        
        self.flight_id = flight_id

class Airline(Base, CustomSerializerMixin):
    __tablename__ = 'airline'

    airline_id = Column(String(), nullable=False, primary_key = True, name = 'ticket_id', default=lambda: str(uuid.uuid4()))
    airline_name = Column(String(), nullable=False)
    country = Column(String(), nullable=False)
    iso31661_alpha2 = Column(String(), nullable=False)
    iso31661_alpha3 = Column(String(), nullable=False)
    iata = Column(String(), nullable=False)
    icao = Column(String(), nullable=False)
    carriage_class = Column(String(), nullable=False)
    call_center = Column(String(), nullable=False)
    admin_id = Column(String(), ForeignKey('admin.admin_id'), nullable=True)
    flight_id = Column(String(), ForeignKey('flight.flight_id'), nullable=False)
    plane_id = Column(String(), ForeignKey('plane.plane_id', ondelete='CASCADE'), nullable=False)

    def __init__(self, airline_name, country, iso31661_alpha2, iso31661_alpha3, iata, icao, carriage_class, call_center, admin_id, flight_id, plane_id, airline_id = None):
        if airline_id:
            self.airline_id = airline_id
        self.airline_name = airline_name
        self.country = country
        self.iso31661_alpha2 = iso31661_alpha2
        self.iso31661_alpha3 = iso31661_alpha3
        self.iata = iata
        self.icao = icao
        self.carriage_class = carriage_class
        self.call_center = call_center
        self.admin_id = admin_id
        self.flight_id = flight_id
        self.admin_id = plane_id