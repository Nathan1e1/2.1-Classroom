# The runner contains the code to Create a User Interface for the Cafe to interact with
# This 'runs' the code and will interact with the Controller directly

from db import createCursor
from service import *
from controller import *
import sqlite3 

conn = sqlite3.connect("order.db")

cursor = conn.cursor()
# creating a table
# cursor.execute("CREATE TABLE new (order_id INTEGER PRIMARY KEY AUTOINCREMENT, customer_name VARCHAR(30), coffee VARCHAR(30), temperature VARCHAR(20), SIZE VARCHAR(20), price DECIMAL)")
# conn.commit()
query = f"INSERT INTO orders values('1', 'abdul', 'flat', '80', 'L', '9.00')"
cursor.execute(query)
conn.commit()

# conn = connectDB('order.db')
# cursor = createCursor(conn)
# s = services(cursor=cursor)
# s.addOrder(coffee="flat",customer_name="abdul",temperature=80,size="L",price=9.00)
print("""
-------- Welcome to QA Cafe --------

What can we help you with?
1) Add Order
2) Read Order By ID
3) Read All Orders
4) Update Order by ID
5) Delete Order by ID
6) Delete All Orders
""")