import requests

data = [
    {"title": "Harry Potter and Prisoner of Azkaban", "year": 2004, "rating": 10, "notes": "Loved it, Harry is the best",},
]

for item in data:
    r = requests.post('http://127.0.0.1:8000/api/movies/', json=item)
    print(r.status_code)
