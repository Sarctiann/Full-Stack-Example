from flask import Flask, jsonify, request
from flask_cors import CORS

from src.extensions import mysql, redis
from src.query_funcs import query
from src.test_data.upload_test_data import load_data


app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pass123'
app.config['MYSQL_DB'] = 'test_project'

app.config['REDIS_URL'] = "redis://redis:6379/0"

mysql.init_app(app)
redis.init_app(app)
CORS(app)


"""
    For the simplicity agreed between the project and this application. 
    I preferred to do the URLs below, avoiding the "Blueprints" implementation 
    that would normally be used in a Flask project.
"""

@app.route('/get_car')
def index():
    plate = request.args.get('plate')
    res = {}
    if plate:
        rowcount, (carmatch, *_) = query('get_car', (plate,))
        if rowcount:
            res['car'] = {
                'id': carmatch[0],
                'plate': carmatch[1],
                'name': carmatch[2]
            }
    return jsonify(res)


@app.route('/initialize')
def upload_data():
    res = load_data()
    return jsonify(res)


@app.route('/mysql_instance')
def dbs():
    res = {}
    res['DATABASES'] = ', '.join([x[0] for x in query('show_dbs')])
    res['TABLES'] = ', '.join([x[0] for x in query('show_tables')])
    return jsonify(res)


# SERVE FRONTEND
@app.route('/')                         # CATCH ALL ROUTES
@app.errorhandler(404)                  # ENABLE RACT ROUTES
def serve(_=None):
    # Discart error
    return '<h1> No found for now</h1>'