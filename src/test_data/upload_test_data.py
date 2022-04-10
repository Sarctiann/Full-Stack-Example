"""
    This script looks for the TEST_DATA.csv file, and loads to the database,
    make sure you have the database running.
"""

import csv
import time

from src.query_funcs import query



def load_data():
    # Check if cars table exists and if not, create it
    res = {}
    try:
        tables = [x[0] for x in query('show_tables')]
        res['actual_tables'] = tables
        if 'cars' not in tables:
            res['table_created'] = query(
                'create_cars_table'
            ) or 'cars table was created'

    except Exception as exc:
            res['error'] = str(exc)
        
    with open('./src/test_data/TEST_DATA.csv', 'r') as f:
        data = [tuple(x, ) for x in csv.reader(f)]
        res['data_to_load'] = str(data)

    res['data_loaded'] = query('upload_data', data, many=True)

    return res
    