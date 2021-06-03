DROP DATABASE IF EXISTS dneprairport;
CREATE DATABASE dneprairport;
\c dneprairport

CREATE TABLE admin(
  admin_id text PRIMARY KEY NOT NULL,
  last_name text NOT NULL,
  first_name text NOT NULL,
  patronymic text NOT NULL,
  password text NOT NULL
);

CREATE TABLE plane(
  plane_id text PRIMARY KEY NOT NULL,
  plane_name text NOT NULL,
  kol_seats bigint NOT NULL
);

CREATE TABLE orders(
  order_id text PRIMARY KEY NOT NULL,
  last_name text NOT NULL,
  first_name text NOT NULL,
  date_of_birthday date NOT NULL,
  num_passport bigint NOT NULL,
  valid_until date NOT NULL,
  email text NOT NULL
);

CREATE TABLE transplantation(
  transplantation_id text PRIMARY KEY NOT NULL,
  transplantation_date timestamp with time zone NOT NULL,
  gate text NOT NULL,
  company_transfer text NOT NULL
);

CREATE TABLE arrival_flight(
  arrival_id text PRIMARY KEY NOT NULL,
  direction text NOT NULL,
  arrival_date timestamp with time zone NOT NULL,
  terminal text NOT NULL,
  gate text NOT NULL,
  remark text NOT NULL,
  airport_name text NOT NULL
);

CREATE TABLE departure_flight(
  departure_id text PRIMARY KEY NOT NULL,
  real_time timestamp with time zone NOT NULL,
  terminal text NOT NULL,
  gate text NOT NULL,
  remark text NOT NULL,
  airport_name text NOT NULL
);

CREATE TABLE flight(
  flight_id text PRIMARY KEY NOT NULL,
  direction text NOT NULL,
  departure_date timestamp with time zone NOT NULL,
  airline_name text NOT NULL,
  arrival_id text NOT NULL,
  departure_id text NOT NULL,
  transplantation_id text NOT NULL,
  FOREIGN KEY(arrival_id) REFERENCES arrival_flight(arrival_id) ON DELETE CASCADE,
  UNIQUE(arrival_id),
  FOREIGN KEY(departure_id) REFERENCES departure_flight(departure_id) ON DELETE CASCADE,
  UNIQUE(departure_id),
  FOREIGN KEY(transplantation_id) REFERENCES transplantation(transplantation_id) ON DELETE CASCADE
);

CREATE TABLE ticket(
  ticket_id text PRIMARY KEY NOT NULL,
  air_ticket_class text NOT NULL,
  order_id text,
  flight_id text NOT NULL, 
  FOREIGN KEY(order_id) REFERENCES orders(order_id) ON DELETE CASCADE, 
  FOREIGN KEY(flight_id) REFERENCES flight(flight_id) ON DELETE CASCADE
);

CREATE TABLE airline(
  airline_id text PRIMARY KEY NOT NULL,
  airline_name text NOT NULL,
  country text NOT NULL,
  iso31661_alpha2 text NOT NULL,
  iso31661_alpha3 text NOT NULL,
  iata text NOT NULL,
  icao text NOT NULL,
  carriage_class text NOT NULL,
  call_center text NOT NULL,
  admin_id text,
  flight_id text NOT NULL,
  plane_id text NOT NULL,
  FOREIGN KEY(admin_id) REFERENCES admin(admin_id),
  FOREIGN KEY(flight_id) REFERENCES flight(flight_id),
  FOREIGN KEY(plane_id) REFERENCES plane(plane_id) ON DELETE CASCADE
);