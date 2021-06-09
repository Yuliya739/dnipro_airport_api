# dnipro_airport_api

## Docs

### GET /departure/today
returns 200

response body

    [
        {
            "airline_id": "854e9277-9563-4c5f-8c78-a7db124939de",
            "airport_name": "Borispol",
            "direction": "test",
            "estimated_time": "2021-06-05T15:50:00+03",
            "flight_id": "IX 2356",
            "gate": "3D",
            "is_departure": true,
            "real_time": "2021-06-05T15:51:00+03",
            "remark": "departs at 12:00",
            "terminal": "D4"
        }
    ]


### GET /arrival/today
returns 200

response body

    [
        {
            "airline_id": "854e9277-9563-4c5f-8c78-a7db124939de",
            "airport_name": "Borispol",
            "direction": "test",
            "estimated_time": "2021-06-05T15:50:00+03",
            "flight_id": "IH 5223",
            "gate": "4A",
            "is_departure": false,
            "real_time": "2021-06-05T15:51:00+03",
            "remark": "departs at 12:00",
            "terminal": "3B"
        },
        {
            "airline_id": "854e9277-9563-4c5f-8c78-a7db124939de",
            "airport_name": "Borispol",
            "direction": "test",
            "estimated_time": "2021-06-05T15:50:00+03",
            "flight_id": "MW 2214",
            "gate": "4A",
            "is_departure": false,
            "real_time": "2021-06-05T15:51:00+03",
            "remark": "departs at 12:00",
            "terminal": "3B"
        },
    ]

### PUSH /flight
request body

    {
        "is_departure": true, 
        "estimated_time": "2012-11-01T04:16:13-04:00",
        "direction": "test", 
        "real_time": "2012-11-01T04:16:18-04:00", 
        "terminal": "D4", 
        "plane_id": "854e9277-9563-4c5f-8c78-a7db124939de", 
        "gate": "3D", 
        "remark": "departs at 12:00", 
        "airport_name": "Borispol",
        "travel_time": 180
    }

returns 200

response body

    flight_id

### GET /flight
returns 200

response body

    [
        {
            "airline_id": "854e9277-9563-4c5f-8c78-a7db124939de",
            "airport_name": "Borispol",
            "direction": "test",
            "estimated_time": "2012-11-01T10:16:13+02",
            "flight_id": "MN 7074",
            "gate": "3D",
            "is_departure": true,
            "real_time": "2012-11-01T10:16:18+02",
            "remark": "departs at 12:00",
            "terminal": "D4"
        },
        {
            "airline_id": "854e9277-9563-4c5f-8c78-a7db124939de",
            "airport_name": "Borispol",
            "direction": "test",
            "estimated_time": "2012-11-01T10:16:13+02",
            "flight_id": "VK 5045",
            "gate": "3D",
            "is_departure": true,
            "real_time": "2012-11-01T10:16:18+02",
            "remark": "departs at 12:00",
            "terminal": "D4"
        }
    ]

### PUSH /airline
request body

    {
        "airline_name": "test2",
        "country": "test2",
        "iso31661_alpha2": "test2",
        "iso31661_alpha3": "test2",
        "iata": "test2",
        "icao": "test2",
        "carriage_class": "test2",
        "call_center": "test2"
    }

returns 200

response body

    "Done"

### GET /airline
returns 200

response body

    [
        {
            "airline_id": "854e9277-9563-4c5f-8c78-a7db124939de",
            "airline_name": "test",
            "call_center": "test",
            "carriage_class": "test",
            "country": "test",
            "iata": "test",
            "icao": "test",
            "iso31661_alpha2": "test",
            "iso31661_alpha3": "test"
        },
        {
            "airline_id": "6cb31147-4d64-42b7-9217-71434153a9f2",
            "airline_name": "test2",
            "call_center": "test2",
            "carriage_class": "test2",
            "country": "test2",
            "iata": "test2",
            "icao": "test2",
            "iso31661_alpha2": "test2",
            "iso31661_alpha3": "test2"
        }
    ]