import mysql.connector

mysql = mysql.connector.connect(
host="localhost", 
username="root", 
password="afreen1408", 
database="school"
) 
my_cursor = mysql.cursor() 

quary = "DELETE FROM students WHERE PersonID = 5 "

my_cursor.execute(quary)

mysql.commit()

print("data is deleted")