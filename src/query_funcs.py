""" This module contains the funtions to interact with sql and redis """

import time

from src.extensions import mysql, redis


def query(sql_file, params=None, many=False):
    """
        This function performs a query to mysql database
        Recives: A file name (One of the SQL Folder)
            Optional: 
                - params: to pass VALUES to the query
                - many=True: to use "executemany"
        Returns: 
            - without params: cursor fetched data
            - with params:    cursor row count
    """

    retries = 5 
    while True:
        
        try:
            cur = mysql.connection.cursor()
            with open(f'./src/SQL/{sql_file}.sql', 'r') as query:
                if params and many:
                    cur.executemany(query.read(), params)
                    mysql.connection.commit()
                    return cur.rowcount
                elif params:
                    cur.execute(query.read(), params)
                    mysql.connection.commit()
                    return cur.rowcount
                else:
                    cur.execute(query.read())
                    return cur.fetchall()

        except Exception as exc:
            if retries == 0:
                return str(exc)
            retries -= 1
            time.sleep(0.5)


def get_hit_count():
    retries = 5 
    while True:
        try:
            return redis.incr('hits')
        except Exception as exc:
            if retries == 0:
                return str(exc)
            retries -= 1
            time.sleep(0.5)
