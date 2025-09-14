import streamlit as st
import pickle
import numpy as np

model_path = r"C:\Users\Dell\Downloads\best_model.pkl"
scaler_path = r"C:\Users\Dell\Downloads\scaler.pkl"

with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(scaler_path, "rb") as f:
    scaler = pickle.load(f)

    

st.title("Churn Prediction App")

st.divider()

st.write("please enter the values and hit the predict button for getting a prediction. ")

st.divider()

gender = st.selectbox("Enter the gender",["Male","Female"])
senior_citizen = st.radio("Are you a senior citizen?",options=[0,1],format_func=lambda x:"Yes" if x == 1 else "No")
Partner = st.selectbox("Do you have a partner?",["Yes","No"])
Dependents = st.selectbox("Do you have any dependents?",["Yes","No"])
Tenure = st.number_input("Enter tenure",min_value=0,max_value=130,value=10)
phone_service = st.selectbox("Do you have phone service?",["Yes","No"])
Multiple_lines = st.selectbox("Do you have multiple lines?",["Yes","No","No phone service"])
Internet_service = st.selectbox("Do you have internet service?",["DSL","Fibre optics","No"])
Online_security = st.selectbox("Do you have online security?",["Yes","No","No internet service"])
Online_backup = st.selectbox("Do you have online backup?",["Yes","No","No internet service"])
Device_protection = st.selectbox("Do you have device protection?",["Yes","No","No internet service"])
Tech_support = st.selectbox("Do you have tech support?",["Yes","No","No internet service"])
Streaming_TV = st.selectbox("Do you have streaming TV?",["Yes","No","No internet service"])
Streaming_movies = st.selectbox("Do you have streaming movies?",["Yes","No","No internet service"])
Contract = st.selectbox("Do you have contract?",["month-to-month","one year","two year"])
Paperless_billing = st.selectbox("Do you have paperless billing?",["Yes","No"])
Payment_method = st.selectbox("what kind of payment method you use?",["mailed check","electronic check","credit card(automatic)","bank transfer(automatic)"])
Monthly_charges = st.number_input("Enter monthly charge",min_value=0.0,max_value=500.0,value=50.0,step=0.1)
Total_charges = st.number_input("Enter total charge",min_value=0.0,max_value=10000.0,value=50.0,step=10.0)

st.divider()

Predictbutton = st.button("Predict!")

if Predictbutton:
    gender_selected = 1 if gender=="Female" else 0
    Partner_selected = 1 if Partner=="Yes" else 0
    Dependents_selected = 1 if Dependents=="Yes" else 0
    Phone_service_selected = 1 if phone_service =="Yes" else 0
    Multiple_lines_selected = 1 if Multiple_lines=="Yes" else (2 if Multiple_lines == "No phone service" else 0)
    Internet_service_selected = 1 if Internet_service=="DSL" else (2 if Internet_service == "Fibre optics" else 0)
    Online_security_selected = 1 if Online_security=="Yes" else (2 if Online_security == "No internet service" else 0)
    Online_backup_selected = 1 if Online_backup=="Yes" else (2 if Online_backup == "No internet service" else 0)
    Device_protection_selected = 1 if Device_protection=="Yes" else (2 if Device_protection== "No internet service" else 0)
    Tech_support_selected = 1 if Tech_support=="Yes" else (2 if Tech_support == "No internet service" else 0)
    Streaming_TV_selected = 1 if Streaming_TV=="Yes" else (2 if Streaming_TV == "No internet service" else 0)
    Streaming_movies_selected = 1 if Streaming_movies=="Yes" else (2 if Streaming_movies == "No internet service" else 0)
    Contract_selected = 1 if Contract=="one year" else (2 if Contract == "two year" else 0)
    Paperless_billing_selected = 1 if Paperless_billing=="Yes" else 0
    Payment_method_selected = 1 if Payment_method == "mailed check" else (2 if Payment_method == "electronic check" else (3 if Payment_method == "credit card(automatic)" else 0))

    X = [gender_selected,senior_citizen,Partner_selected,Dependents_selected,Tenure,Phone_service_selected,Multiple_lines_selected,Internet_service_selected,Online_security_selected,Online_backup_selected,Device_protection_selected,Tech_support_selected,Streaming_TV_selected,Streaming_movies_selected,Contract_selected,Paperless_billing_selected,Payment_method_selected,Monthly_charges,Total_charges]

    numerical_features = [X[4], X[17], X[18]]
    scaled_numerical = scaler.transform([numerical_features])[0]

    X_scaled = X.copy()
    X_scaled[4] = scaled_numerical[0]
    X_scaled[17] = scaled_numerical[1]
    X_scaled[18] = scaled_numerical[2]

    X_array = np.array([X_scaled]) 
    Prediction = model.predict(X_array)[0]

    predicted = "Churn" if Prediction == 1 else "Not churn"

    st.write(f"Predicted:{predicted}")
else: 

    st.write("please enter values and use predict button")


