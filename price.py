import streamlit as st
import pandas as pd
import numpy as np
import pickle  # Assuming the model is saved as a pickle file

# Load the trained model (assuming it's saved as 'final_regressor.pkl')
with open("C:/Users/ncssa/final_regressor.pkl", 'rb') as model_file:
    final_regressor = pickle.load(model_file)

# Streamlit app
st.set_page_config(layout="wide")
st.title("Car Price Prediction App")
st.subheader("Enter the car details below:")

# Input fields for car features
# Define possible values for Kilometers Driven
km_options = list(range(0, 500001, 1000))  # 0 to 500000 km in steps of 1000 km

# Dropdown selection for Kilometers Driven
km = st.selectbox("Kilometers Driven", km_options, index=km_options.index(13000))

ownerNo = st.sidebar.selectbox("Number of Owners", (1, 2, 3, 4))
years = list(range(1990, 2025))
modelYear = st.sidebar.selectbox("Model Year", years, index=years.index(2020))


# Define possible values for Engine Displacement, Top Speed, and Mileage
displacement_options = list(range(500, 5001, 100))  # 500 to 5000 cc in steps of 100
top_speed_options = list(range(100, 301, 10))      # 100 to 300 km/h in steps of 10
mileage_options = list(range(5, 31))                # 5 to 30 km/l

# Dropdown selection for Engine Displacement
displacement = st.selectbox("Engine Displacement (cc)", displacement_options, index=displacement_options.index(1400))

# Dropdown selection for Top Speed
top_speed = st.selectbox("Top Speed (km/h)", top_speed_options, index=top_speed_options.index(180))

# Dropdown selection for Mileage
mileage = st.selectbox("Mileage (km/l)", mileage_options, index=mileage_options.index(17))
seating_capacity = st.sidebar.selectbox("Seating Capacity", (2,3,4,5,6,7,8,9))

# Encoding for categorical fields
transmission_manual = st.sidebar.selectbox("Transmission", ("Manual", "Automatic"))
fuel_type = st.sidebar.selectbox("Fuel Type", ("Diesel", "Electric", "LPG", "Petrol"))
city = st.sidebar.selectbox("City", ("Chennai", "Delhi", "Hyderabad", "Jaipur", "Kolkata"))

# Convert categorical inputs into the same format used for training
transmission_manual = 1 if transmission_manual == "Manual" else 0
fuel_type_dict = {"Diesel": [0, 0, 0], "Electric": [1, 0, 0], "LPG": [0, 1, 0], "Petrol": [0, 0, 1]}
fuel_type_values = fuel_type_dict[fuel_type]
city_dict = {"Chennai": [1, 0, 0, 0, 0], "Delhi": [0, 1, 0, 0, 0], "Hyderabad": [0, 0, 1, 0, 0],
             "Jaipur": [0, 0, 0, 1, 0], "Kolkata": [0, 0, 0, 0, 1]}
city_values = city_dict[city]

# Create a DataFrame with user inputs
input_data = pd.DataFrame({
    'km': [km],
    'ownerNo': [ownerNo],
    'modelYear': [modelYear],
    'Displacement': [displacement],
    'Top Speed': [top_speed],
    'Mileage': [mileage],
    'Seating Capacity': [seating_capacity],
    'transmission_Manual': [transmission_manual],
    'Fuel Type_Electric': [fuel_type_values[0]],
    'Fuel Type_LPG': [fuel_type_values[1]],
    'Fuel Type_Petrol': [fuel_type_values[2]],
    'city_Chennai': [city_values[0]],
    'city_Delhi': [city_values[1]],
    'city_Hyderabad': [city_values[2]],
    'city_Jaipur': [city_values[3]],
    'city_Kolkata': [city_values[4]]
})

# Predict the car price
if st.button("Predict Price"):
    prediction = final_regressor.predict(input_data)
    st.write(f"The predicted price of the car is: Rs{prediction[0]:,.2f}")
