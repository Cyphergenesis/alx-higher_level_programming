import MySQLdb
import sys

def list_states(username, password, database):
    try:
        # Connect to the MySQL server
        connection = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306
        )
        
        # Create a cursor object to interact with the database
        cursor = connection.cursor()
        
        # Execute the SQL query to retrieve the states
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        
        # Fetch all the rows
        states = cursor.fetchall()
        
        # Display the results
        for state in states:
            print(state)
        
        # Close the cursor and connection
        cursor.close()
        connection.close()
    
    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)
    
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    
    list_states(mysql_username, mysql_password, database_name)

