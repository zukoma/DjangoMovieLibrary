import requests

data = [
    {"title": "TestMovie2", "year": 1999, "notes": "test", "genre": [1]},
    {"title": "TestMovie3", "year": 1999, "notes": "test", "genre": [1]},
]

for item in data:
    r = requests.post('http://127.0.0.1:8000/api/movies/', json=item)
    print(r.status_code)
