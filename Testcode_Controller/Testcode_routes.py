from __main__ import app
from flask import Flask, render_template, url_for, request

@app.route("/")
def testcode():
    return render_template('Testcode_Template/Testcode_index.html')