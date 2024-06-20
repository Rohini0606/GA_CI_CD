from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return("<p>Hello world! </p>")

@app.route("/ping")
def pinger():
    return("<p>Hello  I am under water! </p>")

