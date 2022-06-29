from __main__ import app
from flask import Flask, render_template, url_for, request


@app.route("/dashboard")
def dashboard():
    return render_template('Dashboard_Template/Dashboard_index.html')
