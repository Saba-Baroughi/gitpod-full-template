import psycopg2

# Replace "saba" with your PostgreSQL password
# Replace "chinook" with your actual database name
connection_string = "postgresql://postgres:saba@localhost:5432/chinook"

connection = psycopg2.connect(connection_string)

# build a cursor object of the database
cursor = connection.cursor()

try:
    # Query 1 - select all records from the "Artist" table
    cursor.execute('SELECT * FROM "Artist"')

    # fetch the results (multiple)
    results = cursor.fetchall()

    # print results
    print("Query 1 - All records from the 'Artist' table:")
    for result in results:
        print(result)

 

    

except psycopg2.Error as e:
    print(f"Error: {e}")

finally:
    # close the connection
    if connection:
        connection.close()