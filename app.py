import streamlit as st
import numpy as np
import pickle

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

st.title( "House Price Prediction")

st.write("Enter the details below:")

# Inputs
longitude = st.number_input("Longitude", value=-122.23)
latitude = st.number_input("Latitude", value=37.88)
housing_median_age = st.number_input("House Age", value=41.0)
households = st.number_input("Households", value=126.0)
median_income = st.number_input("Median Income", value=8.3252)

rooms_per_household = st.number_input("Rooms per Household", value=6.9)
bedrooms_per_room = st.number_input("Bedrooms per Room", value=0.14)
population_per_household = st.number_input("Population per Household", value=2.5)

# Ocean selection
ocean = st.selectbox(
    "Ocean Proximity",
    ["<1H OCEAN", "INLAND", "NEAR OCEAN", "NEAR BAY", "ISLAND"]
)

# Convert to one-hot
ocean_features = [0, 0, 0, 0, 0]

if ocean == "<1H OCEAN":
    ocean_features[0] = 1
elif ocean == "INLAND":
    ocean_features[1] = 1
elif ocean == "ISLAND":
    ocean_features[2] = 1
elif ocean == "NEAR BAY":
    ocean_features[3] = 1
elif ocean == "NEAR OCEAN":
    ocean_features[4] = 1

# Prediction button
if st.button("Predict Price"):
    features = np.array([[longitude, latitude, housing_median_age,
                          households, median_income,
                          rooms_per_household, bedrooms_per_room,
                          population_per_household] + ocean_features])

    prediction = model.predict(features)

    st.success(f"Estimated Price: ${prediction[0]:,.2f}")