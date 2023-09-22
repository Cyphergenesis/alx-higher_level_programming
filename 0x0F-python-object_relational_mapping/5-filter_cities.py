import MySQLdb
import sys

def filter_cities_by_state(username, password, database, state_name):
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
        
        # Define the SQL query with placeholders for state_name
        sql_query = """
            SELECT GROUP_CONCAT(name SEPARATOR ', ')
            FROM cities
            WHERE state_id = (
                SELECT id
                FROM states
                WHERE name = %s
            )
            ORDER BY cities.id ASC
        """
        
        # Execute the SQL query with the provided state_name
        cursor.execute(sql_query, (state_name,))
        
        # Fetch the result
        cities_result = cursor.fetchone()
        
        if cities_result and cities_result[0]:
            print(cities_result[0])
        else:
            print()
        
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
    
    filter_cities_by_state(mysql_username, mysql_password, database_name, state_name)

