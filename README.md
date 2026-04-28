# house-price-prediction
House Price Prediction
Overview

This project focuses on predicting house prices using Machine Learning. It analyzes various features like area, number of rooms, and location to estimate the price of a house accurately.

Features
Data cleaning and preprocessing
Exploratory Data Analysis (EDA)
Feature selection and engineering
Model training and evaluation
User input-based price prediction
Tech Stack
Python
Pandas
NumPy
Matplotlib / Seaborn
Scikit-learn
Streamlit (for web app)
Project Structure
House-Price-Prediction/
│── data/              # Dataset files
│── notebooks/         # Jupyter notebooks
│── models/            # Saved models
│── app.py             # Streamlit app
│── requirements.txt   # Dependencies
│── README.md
Dataset

The dataset includes the following features:

Area (sq ft)
Number of bedrooms
Number of bathrooms
Location
Price

(You can mention dataset source like Kaggle if needed)

Installation
Clone the repository:
git clone https://github.com/your-username/House-Price-Prediction.git
cd House-Price-Prediction
Install dependencies:
pip install -r requirements.txt
Run the Project
Run Streamlit App:
streamlit run app.py
Models Used
Linear Regression
Decision Tree Regressor
Random Forest Regressor
Evaluation Metrics
Mean Absolute Error (MAE)
Mean Squared Error (MSE)
R² Score
Output

The model predicts house prices based on user inputs and displays the result through a simple interface.

Future Enhancements
Hyperparameter tuning
Use advanced models like XGBoost
Deploy on cloud (AWS / Azure)
Add more real-world features
Author

Meghana Talapaneni

Acknowledgements
Scikit-learn Documentation
Open datasets (Kaggle)
