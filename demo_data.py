import os
import sqlite3
from query_function import query_and_print

"""
THIS is the output from your queries as docstring comments

$ python demo_data.py
1. Count how many rows you have - it should be 3!
(3,)
2. How many rows are there where both `x`,`y` are at least 5?
(0,)
3. How many unique values of `y` are there ?
(2,)
"""


# Open Connection to new database file
DB_FILEPATH = 'demo_data.sqlite3'
connection = sqlite3.connect(DB_FILEPATH)
cursor = connection.cursor()

#Drop Table if the table exists
cursor.execute('DROP TABLE IF EXISTS demo;')

# Create table
create_table_query = """
CREATE TABLE IF NOT EXISTS demo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    s VARCHAR(20),
    x INT,
    y INT
);
"""
cursor.execute(create_table_query)

# Insert data into table 
data_to_input = [
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7)
]

for row in data_to_input:

    insert_query = f'''
        INSERT INTO demo
        (s, x, y)
        VALUES {row}
    '''
    cursor.execute(insert_query)
connection.commit()


# queries
# 1. Count how many rows you have - it should be 3!
query = 'SELECT COUNT(*) as number_of_rows FROM demo;'
print_query = "1. Count how many rows you have - it should be 3!"
query_and_print(query, print_query, cursor)

# 2. How many rows are there where both `x` and `y` are at least 5?
query = 'SELECT COUNT(*) FROM demo WHERE x < 5 and y < 5;'
print_query = "2. How many rows are there where both `x`,`y` are at least 5?"
query_and_print(query, print_query, cursor)

# 3. How many unique values of `y` are there ?
query = 'SELECT COUNT(DISTINCT y) FROM demo;'
print_query = "3. How many unique values of `y` are there ?"
query_and_print(query, print_query, cursor)
