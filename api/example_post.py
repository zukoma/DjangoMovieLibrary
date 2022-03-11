import requests

data = [
    {"title": "Harry Potter and Prisoner of Azkaban", "year": 2004, "rating": 10, "notes": "Loved it, Harry is the best"},
    {"title": "Star Wars", "year": 1960, "rating": 5, "notes": "Too much space"},
    {"title": "Nekviesta Meile", "year": 2008, "rating": 1, "notes": "no comments"},
    {"title": "Django Unchained", "year": 1999, "rating": 10, "notes": "Reminds me of Django"},
]

for item in data:
    r = requests.post('http://127.0.0.1:8000/api/', json=item)
    print(r.status_code)

