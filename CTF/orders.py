# initialize the Order object
class Order():
    def __init__(self, order_id, order, order_type, price, quantity):
      self.ID = order_id
      self.order= order
      self.order_type= order_type
      self.price = price
      self.quantity= quantity
 
    def __str__(self):
      return f'Id={self.order_id}, order={self.order}, order_type={self.order_type}, price={self.price}, quantity={self.quantity}'

# orders list
orders = []

# function to add new order
# first parameters is the list to add instance of Order object to
# then make a variable new_order from an object and append it to he list
def add_order(orders, order_id, order, order_type, price, quantity):
    new_order = Order(order_id, order, order_type, price, quantity)
    orders.append(new_order)

# check for best buy/sell order
def best_order(orders):
    best_order_buy = None
    best_order_sell = None
    best_order_buy_total = 0
    best_order_sell_total = 0
    for order in orders:
        if order.order == "Buy" and (best_order_buy is None or order.price > best_order_buy.price):
            best_order_buy = order
            best_order_buy_total = order.price * order.quantity
        if order.order == "Sell" and (best_order_sell is None or order.price > best_order_buy.price):
            best_order_sell = order
            best_order_sell_total = order.price * order.quantity

    print(best_order_buy_total)
    print(best_order_sell_total)


# add orders from the table to the list via add_order function
add_order(orders, "001", "Buy", 'Add', 20.0, 100)
add_order(orders, "002", "Sell", 'Add', 25.0, 200)
add_order(orders, "003", "Buy", 'Add', 23.0, 50)
add_order(orders, "004", "Buy", 'Add', 23.0, 70)
add_order(orders, "003", "Buy", 'Remove', 23.0, 50)
add_order(orders, "005", "Sell", 'Add', 28.0, 100)

best_order(orders)
