from flask import Flask
from src.extensions import mysql, redis
from src.query_funcs import query, get_hit_count


app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pass123'
app.config['MYSQL_DB'] = 'test_project'

app.config['REDIS_URL'] = "redis://redis:6379/0"

mysql.init_app(app)
redis.init_app(app)

"""
    For the simplicity agreed between the project and this application. 
    I preferred to do the URLs below, avoiding the "Blueprints" implementation 
    that would normally be used in a Flask project.
"""

@app.route('/')
def index():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)

@app.route('/aver')
def users():
    return str(query('show_dbs'))