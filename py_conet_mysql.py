import mysql.connector
con = mysql.connector.connect(host="localhost", username="root", password="afreen1408", database="school")
my_cursor = con.cursor()

con.commit()
con.close()

print("connection succesfully created!")
