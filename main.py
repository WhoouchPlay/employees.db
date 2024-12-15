from flask import Flask, render_template

from app.data import db

app = Flask(__name__, static_folder="app/static", template_folder="app/templates")


@app.get("/")
def index():
    return render_template("index.html", title="Головна сторінка")


@app.get("/employees")
def show_employees():
    return render_template("employees.html", **context)