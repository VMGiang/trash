import json
import requests
url = "http://127.0.0.1:5200/predict"
data = json.dumps({'sl': [5.84, 4.38], 'sw': [3.0, 2.16], 'pl': [3.75, 7.65], 'pw': [1.1, 1.23]})
r = requests.post(url, data)
print(r.json())
