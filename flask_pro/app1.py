from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return "<h1 style='color:red'>hi world</h1>"



app.run(debug=True)