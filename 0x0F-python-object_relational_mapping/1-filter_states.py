#!/usr/bin/python3
"""
Msqldb script that lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa.
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    h, p = "localhost", 3306
    u, psw, db_name = argv[1], argv[2], argv[3]

    with MySQLdb.connect(host=h, user=u, passwd=psw, db=db_name, port=p) as db:
        with db.cursor() as cursor_obj:
            query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
            cursor_obj.execute(query)
            names = cursor_obj.fetchall()
            for name in names:
                print(name)
