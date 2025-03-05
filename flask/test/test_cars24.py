import pytest 
from main_app.first_app import app 
import json 

@pytest.fixture
def client():
    return app.test_client()

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200 and \
           response.data.decode() == "This is cars24 prediction app."
    
def test_predict(client):
    headers = {'Content-Type': 'application/json'}
    input = {
        "brand_option": 1,
        "fuel_option": 0,
        "gear_option": 1
    }
    response = client.post("/predict", data = json.dumps(input), \
                           headers = headers)
    rdict = response.get_json()
    assert response.status_code == 200 and \
           float(rdict["price"].split(' ')[-1]) > 0