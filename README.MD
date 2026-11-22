# Customer Churn Prediction

## Overview
This project predicts whether a customer is likely to churn using Machine Learning. It includes data preprocessing, exploratory data analysis, model training, model evaluation, hyperparameter tuning, and a Streamlit web application for interactive predictions.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib

## Project Workflow
- Data preprocessing and cleaning
- Exploratory Data Analysis (EDA)
- Feature encoding
- Train-test split
- Feature scaling using StandardScaler
- Machine Learning model training
- Model evaluation
- Hyperparameter tuning using GridSearchCV
- Model serialization using Joblib
- Interactive prediction using Streamlit

## Machine Learning
This project explores classification algorithms to predict customer churn and uses hyperparameter tuning to improve model selection.

## Streamlit Application
The Streamlit application allows users to input customer information and receive a churn prediction.

## How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/Customer-Churn-Prediction.git
```

### 2. Navigate to the project directory
```bash
cd Customer-Churn-Prediction
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
streamlit run app.py
```

## Project Structure
```text
Customer-Churn-Prediction/
│
├── app.py
├── notebook.ipynb
├── customer_churn_data.csv
├── model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

## Purpose
The objective of this project is to demonstrate an end-to-end Machine Learning workflow, including data analysis, model development, evaluation, and deployment through an interactive web application.
