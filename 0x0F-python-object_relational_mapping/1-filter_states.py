#!/usr/bin/python3
"""
A script that lists all states with a name starting with N from the database

The script takes 3 arguments: mysql username, password and database name
The script connects to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states \
    WHERE name LIKE 'N%';")
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
