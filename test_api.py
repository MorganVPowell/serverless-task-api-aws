import requests

url = "https://YOUR-API-URL/production/task"

r = requests.post(url, json={"title": "test"})
print(r.status_code, r.text)

r = requests.get(url)
print(r.status_code, r.text)