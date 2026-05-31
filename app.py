import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.title("Diabetes Readmission Prediction")
st.write("Enter patient information to predict readmission risk.")

df = pd.read_csv("diabetic_data.csv")
df = df.replace("?", pd.NA)
df = df.drop(columns=["encounter_id", "patient_nbr", "weight", "payer_code", "medical_specialty"], errors="ignore")
df = df.dropna()

y = df["readmitted"].apply(lambda x: 1 if x == "<30" else 0)
X = df.drop("readmitted", axis=1)
X = pd.get_dummies(X)

model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X, y)

st.subheader("Patient Information")

age = st.selectbox("Age", df["age"].unique())
gender = st.selectbox("Gender", df["gender"].unique())
race = st.selectbox("Race", df["race"].unique())

time_in_hospital = st.number_input("Time in hospital", min_value=1, max_value=14, value=3)
num_lab_procedures = st.number_input("Number of lab procedures", min_value=1, max_value=150, value=40)
num_medications = st.number_input("Number of medications", min_value=1, max_value=100, value=10)
number_inpatient = st.number_input("Number of inpatient visits", min_value=0, max_value=20, value=0)
number_emergency = st.number_input("Number of emergency visits", min_value=0, max_value=20, value=0)

if st.button("Predict"):
    input_data = pd.DataFrame([{
        "race": race,
        "gender": gender,
        "age": age,
        "time_in_hospital": time_in_hospital,
        "num_lab_procedures": num_lab_procedures,
        "num_medications": num_medications,
        "number_inpatient": number_inpatient,
        "number_emergency": number_emergency
    }])

    input_data = pd.get_dummies(input_data)
    input_data = input_data.reindex(columns=X.columns, fill_value=0)

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("Prediction: Patient is likely to be readmitted within 30 days.")
    else:
        st.success("Prediction: Patient is not likely to be readmitted within 30 days.")