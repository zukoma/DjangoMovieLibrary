import requests

data = {"title": "118", "year": 1999, "rating": 1, "notes": "Delightful movie"}
r = requests.get('http://127.0.0.1:8000/api/9999')
print(r.status_code)

