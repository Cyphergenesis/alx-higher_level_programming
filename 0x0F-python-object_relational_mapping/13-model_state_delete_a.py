#!/usr/bin/python3
"""Deletes all State objects with a name containing 'a' from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    # Extract the command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create an SQLite database in memory (replace with your MySQL connection string)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(mysql_username, mysql_password, database_name),
                           pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the State objects with names containing 'a'
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    # Delete the selected states
    for state in states_to_delete:
        session.delete(state)

    # Commit the transaction
    session.commit()

    # Close the session
    session.close()

