#!/usr/bin/python3
import MySQLdb
import sys


def filter_states_by_name_starting_with_n(username, password, database):
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = connection.cursor()

    try:
        query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
        cursor.execute(query)

        results = cursor.fetchall()

        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))

    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    filter_states_by_name_starting_with_n(username, password, database)
