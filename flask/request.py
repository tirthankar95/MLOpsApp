import requests
import json

url = "http://127.0.0.1:8080/predict"

data = {
    "brand_option": 1,
    "fuel_option": 0,
    "gear_option": 1
}

headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=json.dumps(data), headers=headers)

try:
    response_data = response.json()
    print(response_data)
except ValueError:
    print("Response content is not valid JSON:", response.text)