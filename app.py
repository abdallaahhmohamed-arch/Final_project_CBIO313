import streamlit as st
import pandas as pd

st.title("Diabetes Readmission Prediction")
st.write("Enter patient information to predict readmission risk.")

st.subheader("Patient Information")

age = st.selectbox("Age", ["[0-10]", "[10-20]", "[20-30]", "[30-40]", "[40-50]", "[50-60]", "[60-70]", "[70-80]", "[80-90]", "[90-100]"])
gender = st.selectbox("Gender", ["Female", "Male"])
race = st.selectbox("Race", ["Caucasian", "AfricanAmerican", "Asian", "Hispanic", "Other"])

time_in_hospital = st.number_input("Time in hospital", 1, 14, 3)
num_lab_procedures = st.number_input("Number of lab procedures", 1, 150, 40)
num_medications = st.number_input("Number of medications", 1, 100, 10)
number_inpatient = st.number_input("Number of inpatient visits", 0, 20, 0)
number_emergency = st.number_input("Number of emergency visits", 0, 20, 0)

if st.button("Predict"):
    risk_score = 0

    if time_in_hospital > 7:
        risk_score += 1
    if num_lab_procedures > 60:
        risk_score += 1
    if num_medications > 20:
        risk_score += 1
    if number_inpatient > 1:
        risk_score += 2
    if number_emergency > 1:
        risk_score += 1

    if risk_score >= 3:
        st.error("Prediction: Patient is likely to be readmitted within 30 days.")
    else:
        st.success("Prediction: Patient is not likely to be readmitted within 30 days.")