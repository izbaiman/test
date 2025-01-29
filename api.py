# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/api/greet", methods=["GET"])
def greet():
    return "message"

if __name__ == "__main__":
    app.run(debug=True)