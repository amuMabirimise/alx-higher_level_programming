#!/usr/bin/python3
import MySQLdb
import sys

if len(sys.argv) != 4:
    print("Usage: {} username password database".format(sys.argv[0]))
    sys.exit(1)

username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

connection = MySQLdb.connect(
    host="localhost", port=3306, user=username, passwd=password, db=database
)

cursor = connection.cursor()

try:
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    results = cursor.fetchall()

    for row in results:
        print(row)

except MySQLdb.Error as e:
    print("MySQL Error: {}".format(e))

finally:
    cursor.close()
    connection.close()
