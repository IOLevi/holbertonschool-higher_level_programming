#!/usr/bin/env python3
#takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa

import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities INNER JOIN states ON cities.state_id=states.id WHERE states.name=%s ORDER BY cities.id ASC", (sys.argv[4],)) # if not this look up escape functionality
    query_rows = cur.fetchall()
    for i, row in enumerate(query_rows):
        if i != len(query_rows) - 1:
            print("".join(row), end=", ")
        else:
            print("".join(row))
    cur.close()
    conn.close()