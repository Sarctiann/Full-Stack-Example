""" This module contains the funtions to interact with sql and redis """

import time
import pickle as pk

from src.extensions import mysql, redis


def query(sql_file, params=None, many=False):
    """
        This function performs a query to mysql database
        Recives: A file name (One of the SQL Folder)
            Optional: 
                - params: to pass VALUES to the query
                - many=True: to use "executemany"
        Returns: 
            - with params and many: cursor row count only
            - with params:          tuple(cursor row count, cursor fetched data)
            - without params:       cursor fetched data
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
                    return cur.rowcount, cur.fetchall()
                else:
                    cur.execute(query.read())
                    return cur.fetchall()

        except Exception as exc:
            if retries == 0:
                return str(exc)
            retries -= 1
            time.sleep(0.5)


def redis_get(key):
    retries = 5 
    while True:
        try:
            pk_value = redis.get(key)
            if pk_value:
                return pk.loads(pk_value)
            return None
        except Exception as exc:
            if retries == 0:
                return str(exc)
            retries -= 1
            time.sleep(0.5)


def redis_set(key, value):
    retries = 5 
    while True:
        try:
            return redis.set(key, pk.dumps(value)) 
        except Exception as exc:
            if retries == 0:
                return str(exc)
            retries -= 1
            time.sleep(0.5)
