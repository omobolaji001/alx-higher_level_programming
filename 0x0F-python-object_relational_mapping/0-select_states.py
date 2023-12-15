#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa
The script takes 3 arguments: username, password and database name
script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states;")
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
