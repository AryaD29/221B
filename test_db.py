
import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=input("Enter your MySQL root password: ")
    )

    if connection.is_connected():
        print("Connected to MySQL successfully!")

    connection.close()

except mysql.connector.Error as error:
    print("Connection failed:", error)
