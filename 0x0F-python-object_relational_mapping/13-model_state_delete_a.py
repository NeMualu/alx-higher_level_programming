#!/usr/bin/python3
"""
Deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa.
Usage: ./13-model_state_delete_a.py <mysql username> /
                                     <mysql password> /
                                     <database name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost/{database}", pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State):
        if "a" in state.name:
            session.delete(state)
    session.commit()

