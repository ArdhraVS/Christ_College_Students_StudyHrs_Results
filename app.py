import streamlit as st
import joblib
model=joblib.load("Logistic_Regression_study_hours_model.pk1")
st.title("Student Pass/Fail based on Study Hours")
hours=st.number_input("Enter Study Hours: ",min_value=0.0, max_value= 15.0, value=5.0)
if st.button("Predict"):
  prediction=model.predict([[hours]])
  if predicted[0]==1:
    st.success("Pass")
  else:
    st.error("Fail")
