#!/usr/bin/python3
''' Select state with names matching arguments'''


if __name__ == '__main__':
    import MySQLdb
    import sys

    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    database = MySQLdb.connect(host='localhost', user=user,
                               passwd=passwd, db=db, port=3306)

    cursor = database.cursor()

    cursor.execute('SELECT cities.id, cities.name, states.name FROM cities\
                   JOIN states\
                   ON cities.state_id = states.id\
                   ORDER BY cities.id ASC')

    for row in cursor.fetchall():
        print(row)
