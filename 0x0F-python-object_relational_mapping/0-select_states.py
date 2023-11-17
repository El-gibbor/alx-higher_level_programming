#!/usr/bin/python3
""" a script that lists all states from the database hbtn_0e_0_usa """

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    host, port = "localhost", 3306
    user_name, password, db_name = argv[1], argv[2], argv[3]

    db_connect = MySQLdb.connect(host, user_name, password, db_name, port)
    cur = db_connect.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    table_rows = cur.fetchall()
    for state in table_rows:
        print(state)
    cur.close()
    db_connect.close()
