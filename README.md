# dnipro_airport_api

## Docs

### GET /admin
returns 200

response body

    [
        {
            "admin_id": "003",
            "first_name": "Vasiliy",
            "last_name": "Kycheryagin",
            "password": "qwerty456",
            "patronymic": "Ivanovich"
        },
        {
            "admin_id": "98074fca-a128-4703-a981-87461570161a",
            "first_name": "user",
            "last_name": "test",
            "password": "Qwerty123",
            "patronymic": "patr"
        }
    ]

### PUSH /admin
request body

    {
        "last_name": "test",
        "first_name": "user",
        "patronymic": "patr",
        "password": "Qwerty123"
    }

returns 200

response body

    "Done"

### PUSH /admin/auth
request body

    {
        "admin_id": "d63fa088-95a2-4d68-99f4-131aa7a1f2e7",
        "password": "Qwerty123"
    }

returns 200

response body

    "Done"

returns 404

response body

    "Error"