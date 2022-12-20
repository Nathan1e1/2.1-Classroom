# The runner contains the code to Create a User Interface for the Cafe to interact with
# This 'runs' the code and will interact with the Controller directly

from db import createCursor
from service import *
from controller import *

conn = connectDB('order')
cursor = createCursor(conn)
s = services(cursor=cursor)
s.addOrder(coffee="flat",customer_name="abdul",temperature="80",size="L",price=9.00)
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