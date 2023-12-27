import psycopg2

# Replace "saba" with your PostgreSQL password
# Replace "chinook" with your actual database name
#connect to "chinook" database
connection_string = "postgresql://postgres:saba@localhost:5432/chinook"

connection = psycopg2.connect(connection_string)

# build a cursor object of the database
cursor = connection.cursor()
# Query 1_ select only the "Name" column  the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')
#Query 3- select only "Queen" from "Artist" table
# cursor.execute('SELECT * FROM "Artist" Where "Name"=%s',["Queen"])
#query 4- select all tracks where the composer is "Queen" from the "Track" table
cursor.execute('SELECT * FROM "Track" WHERE "Composer"=%s',["Queen"])


#fetch the results (multiple)
results=cursor.fetchall()
#fetch the result singal
# results=cursor.fetchone()
#close the connection 
connection.close()
#print results
for result in results:
    print(result)