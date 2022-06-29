from __main__ import app
from flask import Flask, render_template, url_for, request

@app.route("/calendar")
def calendar():
    return render_template('Calendar_Template/Calendar_index.html')