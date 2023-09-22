#!/usr/bin/python3
"""Creates the State "California" with the City "San Francisco" in the database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
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

    # Create the tables in the database
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create the State "California" with the City "San Francisco"
    california = State(name="California", cities=[City(name="San Francisco")])

    # Add the State and City to the session
    session.add(california)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()

