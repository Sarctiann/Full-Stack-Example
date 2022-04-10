""" This module contains the funtions to interact with sql and redis """

import time

from src.extensions import mysql, redis


def query(sql_file, *params):
    """
        This function performs a query to mysql database
        Recives: A file name (One of the SQL Folder)
            Optional: The params to format the query
        Returns: returns the cursor fetched data 
    """

    retries = 5 
    while True:
        
        try:
            cur = mysql.connection.cursor()
            with open(f'./src/SQL/{sql_file}.sql', 'r') as query:
                if params:
                    cur.execute(query.read(), params)
                else:
                    cur.execute(query.read())
            return cur.fetchall()

        except Exception as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


def get_hit_count():
    retries = 5 
    while True:
        try:
            return redis.incr('hits')
        except Exception as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)