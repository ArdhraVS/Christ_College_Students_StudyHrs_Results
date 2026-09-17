import streamlit as st
import joblib

# Load the model
model = joblib.load("LogisticRegression_StudyHours_model.pkl")

st.title("Student Pass/Fail based on Study Hours")

hours = st.number_input("Enter Study Hours: ", min_value=0.0, max_value=15.0, value=5.0)

if st.button("Predict"):
    # predict_proba returns [[prob_of_fail, prob_of_pass]]
    probabilities = model.predict_proba([[hours]])[0]
    fail_percentage = probabilities[0] * 100
    pass_percentage = probabilities[1] * 100
    
    # Get the final prediction (0 for Fail, 1 for Pass)
    prediction = model.predict([[hours]])
    
    if prediction[0] == 1:
        st.success(f"Pass ({pass_percentage:.2f}% confidence)")
    else:
        st.error(f"Fail ({fail_percentage:.2f}% confidence)")

