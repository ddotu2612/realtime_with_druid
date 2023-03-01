import requests
import json

url = 'http://localhost:8081/druid/indexer/v1/supervisor'
headers = {'Content-Type': 'application/json'}
with open('spec.json', 'r') as f:
    payload = json.load(f)

response = requests.post(url, headers=headers,  json=payload)
# response = requests.post("http://localhost:8081/druid/indexer/v1/supervisor/datastock/terminate", headers=headers)

print(response.text)