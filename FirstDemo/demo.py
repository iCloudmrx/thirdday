import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="yourusername",
    password="yourpassword",
    db="test"
)

print(mydb)
