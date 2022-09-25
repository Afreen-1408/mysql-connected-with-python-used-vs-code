import mysql.connector

mysql = mysql.connector.connect(
host="localhost", 
username="root", 
password="afreen1408", 
database="school"
) 
my_cursor = mysql.cursor() 
  
quary = "update students set FirstName='shaikh', LastName='Zikra' where PersonID = 4 "

my_cursor.execute(quary)

mysql.commit()

print("data is updated")
