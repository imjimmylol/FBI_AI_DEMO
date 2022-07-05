from flask import Flask
from flask import request
from flask import render_template

app = Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/func1")
def func1():
    return render_template("func1.html")

@app.route("/func2")
def func2():
    return render_template("func2.html")

@app.route("/func3")
def func3():
    return render_template("func3.html")

@app.route("/func4")
def func4():
    return render_template("func4.html")

app.run(port=8000)