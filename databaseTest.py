# import mysql.connector
from mysql.connector import (connection)

conn = connection.MySQLConnection(username='root', password='root',host='localhost',database='face_recognition')
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()