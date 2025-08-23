
import sklearn
import streamlit as st
import pickle
import numpy as np

# Load the model

model = pickle.load(open("StudentPerformancePrediction.pkl", "rb"))

st.title("Student Performance Prediction Application")

# Collect user inputs
input_data = {
    "Study Hours per Week": st.number_input("Study Hours per Week"),
    "Attendance Rate": st.number_input("Attendance Rate"),
    "Previous Grades": st.number_input("Previous Grades"),
    }

if st.button("Predict"):
    input_list = [
        input_data["Study Hours per Week"],
        input_data["Attendance Rate"],
        input_data["Previous Grades"],
        ]
    
    prediction = model.predict([input_list])[0]
    st.write("Prediction:", prediction)
    
    # Output
    if prediction == 0:
        st.success("Prediction: Fail")
    else:
        st.error("Prediction: Passed")