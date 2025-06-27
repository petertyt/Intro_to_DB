import mysql.connector
from mysql.connector import Error

try:
    # Establish a connection
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Rock2012.'
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close connection if it was opened
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
