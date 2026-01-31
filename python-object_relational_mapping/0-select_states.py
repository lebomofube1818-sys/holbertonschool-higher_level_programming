#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
Results are sorted in ascending order by states.id using MySQLdb.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and database from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor
    cursor = db.cursor()

    # Execute SQL query to select all states ordered by id ascending
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows
    rows = cursor.fetchall()

    # Print each row as a tuple exactly
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()
