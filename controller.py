# The controller contains functions that takes in data (such as Order Strings or ids) 
# and run the functions in the Service Object that interact with the DB
# The controller will typically convert String data into Order Objects that can be used with the Service functions

# The controller sends and collects data from the Service file, and pushes this data to the Runner which can display said data

# Not complete, but a suggestion of the process

from service import services
from order import order

def read_by_id(id):
    order = services.read_by_id(id)
    return order


# def enter_order():
#     order = int(input("Please enter type of order: "))
#     order_choices = ['1', '2', '3', '4', '5', '6',]
#     if order not in order_choices:
#         return "Please enter a valid order type."

# def add_order():
#     order_id = random.randint(1, 1000)
#     order_choices = ['Espresso', 'Americano', 'Mocha', 'Flat White']
#     order = int(input("Please enter coffee: "))
#     if order not in order_choices:
#         return "Please enter a valid coffee: (Espresso, Americano, Mocha or Flat White)"

# print(enter_order())

# 

def getData(self):
    name = input("Please enter your name: ")
    coffee = input("Please enter your coffee name: ")
    temperature = input("Please enter the temperature of the coffee: ")
    size = input("Please enter the size of your coffee: ")
    cost = float(input("Please enter the price: "))
    order = order(name, coffee, temperature, size, cost)
    return order

def choice(self):

    choice = int(input("Please select an Order from 1 - 6: "))
    if choice == 1:
        order1 = self.getData()
        return self.createOrder(order1)
    elif choice == 2:
        id = int(input("Please enter ID to view: "))
        return self.viewOrderId(id)
    elif choice == 3:
        return self.viewAllOrders()
    elif choice == 4:
        id = int(input("Please enter the ID of the order to update: "))
        order1 =self.getData()
        return self.updateOrder(id, order1)
    elif choice == 5:
        id = int(input("Please enter the ID to delete: "))
        return self.deleteOrder(id)
    elif choice == 6:
        return self.deleteAllOrders()
    else:
        return "Miss input!"

def viewAllOrders(self):
    data = self.services.viewAllOrders()
    return data

def viewOrderId(self, id):
    data = self.service.viewOrderId(id)
    return data

def createOrder(self, order):
    check = self.service.createOrder(order)
    return check

def deleteOrder(self, id):
    check = self.service.delAllOrder()
    return check

def deleteAllOrder(self):
    check = self.service.delAllOrder()
    return check

def deleteAllOrders(self):
    data = self.service.updateOrderId(id, order)
    return data