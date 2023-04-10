


import sqlite3
conn = sqlite3.connect('revenue.db')  # a db connection object

c = conn.cursor()

fh = open('revenue.txt')
lines = fh.read().splitlines()

for line in lines:
    items = line.split(',')
    items[0] = items[0].replace("'", r"''")
    query = "INSERT INTO revenue VALUES('{}', '{}', {})".format(items[0], items[1], items[2])
    c.execute(query)

conn.commit(m)





