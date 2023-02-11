import requests
from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)
app.config['people'] = []
app.config['total_seats'] = 100
app.config['avl_seats'] = 100

@app.route("/flights/avail_seats/")
def flightsavl():
    if app.config['avl_seats'] > 0:
        s = app.config['avl_seats']
    else:
        print("Seats unavailable")
    return render_template(
    'flights.html', **locals())

@app.route("/flights/book/<string:name>/")
def book(name):
    success = False
    if app.config['avl_seats'] > 0 and name not in app.config['people']:
        app.config['people'].append(name)
        app.config['avl_seats'] = app.config['total_seats'] - len(app.config['people'])
        success = True

    return render_template(
        'book.html', **locals())

app.run(host='0.0.0.0', port=80)