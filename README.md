# 🏠 Bangalore House Price Predictor

This is a machine learning web application that predicts housing prices in Bangalore based on user inputs like location, square footage, number of bedrooms (BHK), and number of bathrooms.

Built using Python and Streamlit, the model uses data preprocessing and a trained regression algorithm to estimate property prices.

## 🔍 Features

- 📍 Location-based price prediction
- 📐 Inputs: Total Square Feet, BHK, Bathrooms
- 🧠 Trained ML model (Linear Regression)
- 🌐 Interactive Streamlit web app
- 📊 Future enhancement: Map and data visualizations

## 🛠️ Tech Stack

- Python 🐍
- Pandas, NumPy, Scikit-learn
- Streamlit
- Joblib (for model persistence)
- Git & GitHub (version control)

## 📦 Dataset

Dataset from [Kaggle - Bengaluru House Price Data](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data)

## 📁 Project Structure

bangalore-house-price-predictor/
├── app.py # Streamlit app
├── model_training.ipynb # Notebook used for preprocessing & training
├── bangalore_home_price_model.pkl # Trained ML model
├── model_columns.pkl # Column names used during training
├── requirements.txt # Required Python packages
└── README.md # Project documentation


## 🚀 How to Run Locally

1. Clone the repository:
   git clone https://github.com/sparshshekhar/bangalore-house-price-predictor.git

2. Navigate to the project folder:
    cd bangalore-house-price-predictor

3. Install dependencies:
    pip install -r requirements.txt

4. Run the Streamlit app:
    streamlit run app.py

Author- Sparsh Shekhar


