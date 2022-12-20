# The service file interacts with the DB file to Query or Modify data within the database
# Typically there will be a function for each process that is required, and these will take in data and return data

# Not a complete function, but a suggestion of what to do
# def read_by_id(id):
#     order_data = db.query(id)
#     order = order(order_data) 

from db import connectDB

class services():

    def __init__(self, cursor):
        self.cursor = cursor
    
    def runQuery(self, query):
        data = self.cursor.execute(query)
        return

    def addOrder(self, customer_name, coffee, temperature, size, price):
        query = f"INSERT INTO orders ({customer_name}, {coffee}, {temperature}, {size}, {price})"
        self.runQuery(query)
        return True

    def delOrder(self, id):
        query = f"DELETE FROM orderes WHERE order_id = {id}"
        self.runQuery(query)
        return True

    def viewAllOrders(self):
        query = "SELECT * FROM orders"
        data = self.runQuery(query)
        return data.fetchall()

    def viewOrderId(self, id):
        query = f"SELECT * FROM orders WHERE order id = {id}"
        self.runQuery(query)
        return True