#!/usr/bin/python3
import MySQLdb
import sys


def filter_states_by_name(username, password, database, state_name):
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = connection.cursor()

    try:
        query = (
            "SELECT * FROM states WHERE name = '{}' "
            "ORDER BY id ASC".format(state_name)
        )
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
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name"
              .format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = (
        sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    )

    filter_states_by_name(username, password, database, state_name)
