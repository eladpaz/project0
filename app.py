from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/library")
def library():
    return render_template("library.html")

@app.route("/data")
def data():
    return render_template("data.html")
