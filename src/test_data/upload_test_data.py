"""
    This script looks for the TEST_DATA.csv file, and loads to the database,
    make sure you have the database running.
"""

import csv

with open('./test_data/TEST_DATA.csv', 'r') as f:
    data = [tuple(x) for x in csv.reader(f)]

print(data)