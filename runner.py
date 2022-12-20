# The runner contains the code to Create a User Interface for the Cafe to interact with
# This 'runs' the code and will interact with the Controller directly
import random

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

# order = (input("Please enter type of order: "))

# if order  addOrder:
#     print (" what type of coffee would you like?: ")

def enter_order():
    order = int(input("Please enter type of order: "))
    order_choices = ['1', '2', '3', '4', '5', '6',]
    if order not in order_choices:
        return "Please enter a valid order type."

def add_order():
    order_id = random.randint(1, 1000)
    order_choices = ['Espresso', 'Americano', 'Mocha', 'Flat White']
    order = int(input("Please enter coffee: "))
    if order not in order_choices:
        return "Please enter a valid coffee: (Espresso, Americano, Mocha or Flat White)"

print(enter_order())




