#!/usr/bin/python3
""" connects to a MySQL db and removes rows from the 'State' table
where the letter 'a' is present in the 'name' column."""

from sys import argv
from sqlalchemy.orm import Session
from model_state import Base, State
from sqlalchemy import create_engine

conn_url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"

engine = create_engine(conn_url)
Base.metadata.create_all(engine)

with Session(engine) as session:
    all_states = session.query(State).all()
    for state in all_states:
        if 'a' in state.name:
            session.delete(state)
    session.commit()