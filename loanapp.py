import streamlit as st
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import pickle
import time

st.set_page_config(page_title="Loan App Engine", layout="wide", page_icon=":chart:")

st.title("Loan Predictor App Engine")
st.subheader("A Linear Regression model to predict whether the applicant's loan will be approved or rejected.")

st.text("Test page with interactive tool to check the model run through streamlit.")
st.text("The default values are filled in, please enter your own input to check for your score and other details")
st.write("______________________________________________________________________________________________")

st.image("Loan_Approval_Predictor.png")

st.write("______________________________________________________________________________________________")

gender = st.radio(
        label = 'Select your Gender',
        options=["Male", "Female"]
    )
gender = 0 if gender=='Male' else 1
maritalstatus = st.radio(
        label = 'Marital Status',
        options=["Unmarried", "Married"]
    )
maritalstatus = 1 if maritalstatus=='Married' else 0
applicantincome = st.number_input(
        label = 'State your income',
        min_value= 0,
        value=10000,
    )
credithistory = st.radio(
        label = 'Credit History',
        options=["Cleared all Debts", "Have Uncleared Debts"]
    )
credithistory = 1 if credithistory=='Cleared all Debts' else 0
loanamount = st.number_input(
        label = 'Loan amount you want to apply for',
        min_value= 0,
        value=20000,
    )

if st.button("Predict", type='primary', icon="😃"):
    Gender = gender
    MaritalStatus = maritalstatus
    ApplicantIncome = applicantincome
    CreditHistory = credithistory
    LoanAmount = loanamount

    input_data = np.array([[Gender, MaritalStatus, ApplicantIncome, CreditHistory, LoanAmount]])

    with open("classifier.pkl", 'rb') as f:
        model = pickle.load(f)
    with st.spinner("Predicting..."):
        time.sleep(1)

    prediction = model.predict(input_data)

    #st.success(f"Based on your input, the model predicts that your loan application will {'be approved' if prediction==1 else'rejected'}.")
    if prediction<=0:
        st.markdown(f"<h3 style='color:#a3170a; font-weight:bold;'> Loan applicated REJECTED; Consider refining your application or contacting the loan lender for more information.", unsafe_allow_html=True)
    else:
        st.markdown(f"<h3 style='color:#046e45; font-weight:bold;'> Loan applicated APPROVED; Congratulations!!", unsafe_allow_html=True)
