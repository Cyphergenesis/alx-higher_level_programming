import MySQLdb
import sys

def filter_states_by_name(username, password, database, state_name):
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
        
        # Define the SQL query with a placeholder for state_name
        sql_query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        
        # Execute the SQL query with the provided state_name
        cursor.execute(sql_query, (state_name,))
        
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
    if len(sys.argv) != 5:
        print("Usage: {} <mysql_username> <mysql_password> <database_name> <state_name>".format(sys.argv[0]))
        sys.exit(1)
    
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]
    
    filter_states_by_name(mysql_username, mysql_password, database_name, state_name)

