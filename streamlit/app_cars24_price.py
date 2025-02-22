import streamlit as st
import pickle 
import json 
import sklearn

with open("checkpoint/model.pkl", "rb") as file:
    model = pickle.load(file)

with open("checkpoint/scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

with open("checkpoint/feature_map.json", "r") as file:
    feature_map = json.load(file)

with open("checkpoint/default_values.json", "r") as file:
    default_map = json.load(file)

col1, col2 = st.columns(2)
with col1:
    brand_option = st.selectbox('Car Brand', \
                                (car for car, index in feature_map['Car Brand'].items()),
                                index = int(default_map["Car Brand"]))
    brand_option = feature_map['Car Brand'][brand_option]
    gear_option = st.radio('Gear Type', \
                          (gear for gear, index in feature_map['Gear'].items()), 
                          index = int(default_map['Gear']))
    gear_option = feature_map['Gear'][gear_option]
    driven_option = st.number_input('Driven (in Kms)', 0, 1000000, int(default_map["Driven (Kms)"])) # min_value, max_value, default_value

with col2:
    fuel_option = st.selectbox('Fuel Type', \
                                (car for car, index in feature_map['Fuel'].items()),
                                index = int(default_map["Fuel"]))
    fuel_option = feature_map['Fuel'][fuel_option]
    ownership_option = st.radio('Number of owners', \
                                (1, 2, 3, 4, 5), index = int(default_map["Ownership"])-1) # -1 because index = ownership - 1
    model_year_option = st.slider('Model Year', 2000, 2022, int(default_map["Model Year"])) # min_value, max_value, default_value
    ownership_option = int(ownership_option)


if (st.button('Predict')):

    #Ordering of columns before scaler.fit()
    #['Car Brand', 'Fuel', 'Gear', 'Model Year', 'Driven (Kms)', 'Ownership']

    X = [brand_option, fuel_option, gear_option, model_year_option, driven_option, ownership_option]
    X = scaler.transform([X])
    st.write(f'Rs {round(model.predict(X)[0], 2)}')