# The DB file contains the processes and functions to create our Database or connect to it as well as run the initial SQL
# The DB file should also contain query functions that the Service file can use to read or modify the data

import sqlite3 as sqlite

def connectDB(order):
    conn  = sqlite.connect(order)
    return conn

def createCursor(conn):
    cursor = conn.cursor()
    return cursor

def commitDB(conn):
    conn.commit()
    return True

def createDB(cursor):
    sqlFile = open("orders.sql")
    sqlString = sqlFile.read()
    cursor.executescript(sqlString)
    print(cursor.executre("SELECT name FROM sqlite_master WHERE type='table';").fetchall())

def runCode():
    conn = connectDB("order.db")
    cursor = createCursor(conn)
    commitDB(conn)

# conn = connectDB("order.db")
# cursor = createCursor(conn)
