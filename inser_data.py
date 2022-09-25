import mysql.connector
mysql = mysql.connector.connect(
host="localhost", 
username="root", 
password="afreen1408", 
database="school"
) 
my_cursor = mysql.cursor()

# Queries for retrivint all rows
quary = "insert into students(PersonID,LastName,FirstName,class,divition) values (%s,%s,%s,%s,%s)"
val = (11,"Afreen", "choudhary", "12th", "A")

my_cursor.execute(quary,val)

mysql.commit()

print("data is saved")