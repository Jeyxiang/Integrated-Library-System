#py -m pip install mysql-connector-python

import mysql.connector

def connectTo(hostname, username, user_password, dbname):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = hostname,
            user = username,
            passwd = user_password,
            database = dbname
        )
        print("Connected to MySQL Database: " + dbname)
    except Error as err:
        print("Cannot Connect")

    return connection

def executeQuery(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print("Cannot Execute")

def readQuery(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print("Cannot Read")

##connection = connectTo("localhost", "root", "pwd", "library")
##query1 = """SELECT count(*) FROM borrow WHERE bookID =2;"""
##results = readQuery(connection, query1)
##for result in results:
##    print(result)
