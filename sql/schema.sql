DROP DATABASE IF EXISTS dneprairport;
CREATE DATABASE dneprairport;
\c dneprairport


CREATE TABLE airline(
  airline_id text PRIMARY KEY NOT NULL,
  airline_name text NOT NULL,
  country text NOT NULL,
  iso31661_alpha2 text NOT NULL,
  iso31661_alpha3 text NOT NULL,
  iata text NOT NULL,
  icao text NOT NULL,
  carriage_class text NOT NULL,
  call_center text NOT NULL
);

CREATE TABLE plane(
  plane_id text PRIMARY KEY NOT NULL,
  plane_name text NOT NULL,
  kol_seats bigint NOT NULL,
  airline_id text NOT NULL,
  FOREIGN KEY(airline_id) REFERENCES airline(airline_id)
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

CREATE TABLE flight(
  flight_id text PRIMARY KEY NOT NULL,
  estimated_time timestamp with time zone NOT NULL,
  is_departure boolean DEFAULT TRUE NOT NULL,
  real_time timestamp with time zone NOT NULL,
  terminal text NOT NULL,
  gate text NOT NULL,
  remark text NOT NULL,
  airport_name text NOT NULL,
  direction text NOT NULL,
  airline_id text NOT NULL,
  FOREIGN KEY(airline_id) REFERENCES airline(airline_id) ON DELETE CASCADE
);

CREATE TABLE transplantation(
  transplantation_id text PRIMARY KEY NOT NULL,
  transplantation_date timestamp with time zone NOT NULL,
  gate text NOT NULL,
  company_transfer text NOT NULL,
  flight_id text NOT NULL,
  FOREIGN KEY(flight_id) REFERENCES flight(flight_id) ON DELETE CASCADE
);

CREATE TABLE ticket(
  ticket_id text PRIMARY KEY NOT NULL,
  air_ticket_class text NOT NULL,
  order_id text,
  flight_id text NOT NULL, 
  FOREIGN KEY(order_id) REFERENCES orders(order_id) ON DELETE CASCADE, 
  FOREIGN KEY(flight_id) REFERENCES flight(flight_id) ON DELETE CASCADE
);