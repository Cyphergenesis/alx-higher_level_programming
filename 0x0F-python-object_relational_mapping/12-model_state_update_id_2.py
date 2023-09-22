#!/usr/bin/python3
"""Changes the name of a State object in the database
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

    # Query for the State object with id = 2
    state_to_update = session.query(State).filter_by(id=2).first()

    # Check if the state was found
    if state_to_update:
        # Update the state name to "New Mexico"
        state_to_update.name = "New Mexico"
        # Commit the transaction
        session.commit()

    # Close the session
    session.close()

