# BT2102

### BEFORE RUNNING

Dependencies: Python3, pillow, tkinter, mysql-connector-python, pymongo, dateutil

Tkinter is installed by default with Python3, to install dependencies, run the following commands:
py -m pip install Pillow
py -m pip install mysql-connector-python
py -m pip install pymongo
py -m pip install python-dateutil

Import books.json into db: ils and collection: books
Code: mongoimport --db ils --collection books books.json
Recommended MySQL database: library
MySQL connection setup: edit 3rd(password) and 4th(db name) field inside connectTo inside root.py at line 9

Open root.py ONLY from the file location (NOT from shortcuts, etc)

### WHILE RUNNING

If MongoDB connection fails: edit nosqlaccessors
If MySQL connection fails: check 3rd(password)/4th(db name) field inside connectTo inside root.py at line 9

### CODING GUIDELINES

Date and Time: datetime(year, month, day) to create datetime object in python (ISO8601)
lightblue for main&admin / lightgreen for borrow / palegoldenrod for resvn / thistle for fines / 
peachpuff for mysql books / lavender for mongosearch
Navigation Method Naming: nav1to2()
Font: Mincho

MySQL Queries: executeQuery(connection, query); readQuery(connection, query)
NoSQL Queries: queryMongo(query, *projection); distinctMongo(query)

1: login vs loginF()--> 2/3
2: register vs registerF() --> 1
3: mainMenu --> 4/5/6/8/9/10a
4: borrowMenu --> 3
5: reserveMenu --> 3
6: fineMenu --> 3/7
7: paymentMenu --> 3
8: adminMenu --> 4a/5a/6a/9
9: searchMenu --> 3/10
10: resultMenu --> 3
10a: mySQLBookMenu --> 11
11: bookMenu --> 3