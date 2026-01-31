#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
Results are sorted in ascending order by states.id using MySQLdb.
"""

import MySQLdb
import sys


def list_states(username, password, database):
    """
    Connects to MySQL and returns a list of states
    ordered by id ascending.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    cursor.close()
    db.close()
    return rows


if __name__ == "__main__":
    # Get arguments safely
    if len(sys.argv) != 4:
        sys.exit()

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    states = list_states(username, password, database)
    for state in states:
        print(state)
