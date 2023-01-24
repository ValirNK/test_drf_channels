import requests

r = requests.post('http://127.0.0.1:8000/api/clients', data={
        "name": "Jio 2",
        "adress": "г. ЕКБ, ул. Ленина 1",
        "cart": [
            2,3
        ]
})