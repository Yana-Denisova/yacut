from flask import render_template

from . import app, db


@app.route('/')
def index_view():
    return render_template('index.html')