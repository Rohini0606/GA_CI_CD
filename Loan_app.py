import requests
from flask import Flask, request
import pickle

app = Flask(__name__)

model_pickle = open("./classifier.pkl", "rb")
clf = pickle.load(model_pickle)

@app.route("/")
def hello_world():
    return("<p>Hello world! </p>")

@app.route("/ping")
def pinger():
    return("<p>Hello  I am under water! </p>")

@app.route("/json")
def json_check():
    return({"message" : "Hi I am json"})



@app.route("/predict", methods  = ['POST'])
def prediction():
    loan_req = request.get_json()
    if loan_req['Gender'] == "Male":
        Gender = 0
    else:
        Gender = 1
    if loan_req['Married'] == "Yes":
        Married = 1
    else:
        Married = 0
    ApplicantIncome = loan_req['ApplicantIncome']
    LoanAmount = loan_req['LoanAmount']
    Credit_History = loan_req['Credit_History']

    result = clf.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])
    if result == 0:
        pred = "Rejected"
    else:
        pred = "Approved"
    return {"Loan_approval_status":pred}