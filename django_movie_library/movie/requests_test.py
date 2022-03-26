import requests

data = [
    {"title": "TestMovie", "year": 2004, "rating": 10, "notes": "ok", "genre": [1], "added_by": 1},
    {"title": "TestMovie", "year": 2004, "rating": 10, "notes": "ok", "genre": [1], "added_by": 1},
]

for item in data:
    r = requests.post('http://127.0.0.1:8000/api/movies/', json=item)
    print(r.status_code)
