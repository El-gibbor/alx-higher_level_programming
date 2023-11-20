#!/usr/bin/python3
""" Connects to a MySQL database using SQLAlchemy, retrieves the first entry from the 'states' table,
and prints its ID and name. If the table is empty, it prints "Nothing. """

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy.orm import Session
    from model_state import Base, State
    from sqlalchemy import create_engine

    conn_url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"

    engine = create_engine(conn_url)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        first_state = session.query(State).first()
        if first_state:
            print(f"{first_state.id}: {first_state.name}")
        else:
            print("Nothing")
