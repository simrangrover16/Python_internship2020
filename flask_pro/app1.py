from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return "<h1 style='color:red'>hello world</h1>"

@app.route("/home/")
def home():
    return "hello to my home"

@app.route("/hello/")
def hello():
    return "Python is supernice"


@app.route("/login/")
def login():
    return "Login file"

app.run(debug=True)
