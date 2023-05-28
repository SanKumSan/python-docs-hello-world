from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Santhosh"

@app.route("/test")
def hello1():
    return "Hello Santhosh with Test"
