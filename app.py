from flask import Flask, render_template, url_for, request

app = Flask(__name__)


import Testcode_Controller.Testcode_routes
import Calendar_Controller.Calendar_routes
import Dashboard_Controller.Dashboard_routes

    


if __name__ == '__main__':
    app.run(debug=True)