from flask import Flask, request
import json 
import pickle 
import os 

base_dir = os.path.join(os.getcwd(), "checkpoint")
with open(f"{base_dir}/model.pkl", "rb") as file:
    model = pickle.load(file)

with open(f"{base_dir}/scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

with open(f"{base_dir}/feature_map.json", "r") as file:
    feature_map = json.load(file)

with open(f"{base_dir}/default_values.json", "r") as file:
    default_map = json.load(file)

app = Flask(__name__)
@app.route('/')
def home():
    return 'This is cars24 prediction app.'

@app.route('/predict', methods = ["POST"])
def predict():
    if request.method == 'POST':
        data = request.get_json()
        X = [default_map['Car Brand'] if 'brand_option' not in data else data['brand_option'], \
             default_map['Fuel'] if 'fuel_option' not in data else data['fuel_option'], \
             default_map['Gear'] if 'gear_option' not in data else data['gear_option'], \
             default_map['Model Year'] if 'model_year_option' not in data else data['model_year_option'], \
             default_map['Driven (Kms)'] if 'driven_option' not in data else data['driven_option'], \
             default_map['Ownership'] if 'ownership_option' not in data else data['ownership_option']
            ]
        X = scaler.transform([X])
        return {'price': f'Rs {round(model.predict(X)[0], 2)}'}
    return {'price' f'bad request'}

if __name__ == '__main__':
    app.run(debug=True)