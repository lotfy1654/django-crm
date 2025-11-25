# Install Mysql on my computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql 
# pip install mysql-connector-python
# pip install mysql-connector


import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password123",
    auth_plugin='mysql_native_password'
)

# prepare a cursor object
cursor_object = dataBase.cursor()

# Create a database
cursor_object.execute("CREATE DATABASE crm_db")

print("Database created successfully!")