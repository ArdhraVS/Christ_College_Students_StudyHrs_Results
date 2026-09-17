import streamlit as st
import joblib
model = joblib.load("LogisticRegression_StudyHours_model.pkl")
st.title("Student Pass/Fail based on Study Hours")
hours = st.number_input("Enter Study Hours: ", min_value=0.0, max_value=15.0, value=5.0)
attnd= st.number_input("Enter Attendance: ",min_value=0.0, max_value=100.0, value=75.0)
if st.button("Predict"):
    probabilities = model.predict_proba([[hours,attnd]])[0]
    fail_percentage = probabilities[0] * 100
    pass_percentage = probabilities[1] * 100
    
    prediction = model.predict([[hours,attnd]])
    if prediction[0] == 1:
        st.success("Pass")
        st.write(f"Pass Probability: {pass_percentage:.2f}%")
    else:
        st.error("Fail")
        st.write(f"Fail Probability: {fail_percentage:.2f}%")
