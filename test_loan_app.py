import pytest
from Loan_app import app
@pytest.fixture()
def client():
    return app.test_client()

def test_pinger(client):
    resp = client.get('/ping')
    assert resp.status_code == 200

def test_json(client):
    resp = client.get('/json')
    assert resp.status_code == 200
    assert resp.json == {"message" : "Hi I am json"}

def test_prediction(client):
    test_data = {"ApplicantIncome":1000000,
                 "Credit_History":1.0,
                 "Gender":"Male",
                 "LoanAmount": 12000000,
                 "Married":"Yes"}
    resp = client.post('/predict', json = test_data)
    assert resp.status_code == 200
    assert resp.json == {"Loan_approval_status": "Rejected"}