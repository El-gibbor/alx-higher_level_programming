#!/usr/bin/python3
""" Mysqldb script that takes in an argument and displays all
    values in the states table of hbtn_0e_0_usa where name matches the argument
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    host, port = "localhost", 3306,
    user, passwd, db_name, state_name = argv[1], argv[2], argv[3], argv[4]

    with MySQLdb.connect(host, user, passwd, db_name, port) as db_conn:
        with db_conn.cursor() as cursor_obj:
            query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
            cursor_obj.execute(query, (state_name,))
            fetched_state = cursor_obj.fetchall()
            for state in fetched_state:
                print(state)
