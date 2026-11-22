import streamlit as st
import joblib
import numpy as np

# Load model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Churn Prediction App")

st.divider()

st.write("Please enter the values and hit the Predict button.")

age = st.number_input("Enter age", min_value=10, max_value=100, value=30)

tenure = st.number_input("Enter Tenure", min_value=0, max_value=130, value=10)

monthlycharge = st.number_input("Enter MonthlyCharge", min_value=30, max_value=150)

gender = st.selectbox("Select the gender", ["Male", "Female"])

st.divider()

prediction_button = st.button("Predict!")

st.divider()

if prediction_button:

    gender_selected = 1 if gender == "Female" else 0

    X = [age, gender_selected, tenure, monthlycharge]

    X_array = np.array(X).reshape(1, -1)

    X_scaled = scaler.transform(X_array)

    prediction = model.predict(X_scaled)[0]

    predicted = "Yes (Churn)" if prediction == 1 else "No (Not Churn)"

    st.balloons()

    if prediction == 1:
        st.error(f"Prediction: {predicted}")
    else:
        st.success(f"Prediction: {predicted}")

else:
    st.write("Enter the customer details above and click Predict.")