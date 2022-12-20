# The controller contains functions that takes in data (such as Order Strings or ids) 
# and run the functions in the Service Object that interact with the DB
# The controller will typically convert String data into Order Objects that can be used with the Service functions

# The controller sends and collects data from the Service file, and pushes this data to the Runner which can display said data

# Not complete, but a suggestion of the process

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




def read_by_id(id):
    order = service.read_by_id(id)
    return order
