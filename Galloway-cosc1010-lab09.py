# Rylan Galloway
# UWYO COSC 1010
# Submission Date 11/11/2024
# Lab 09
# Lab Section: 14
# Sources, people worked with, help given to: Danny Keuning
# Your
# Comments
# Here

# Classes
# For this assignment, you will be creating two classes:
# One for Pizza
# One for a Pizzeria


# You will be creating a Pizza class. It should have the following attributes:
# - Size
# - Sauce
# - Toppings, which should be a list
# You need to create one method that corresponds with each of the above attributes
# which returns the corresponding attribute, just the value.
# For the size and toppings attributes, you will need to have a method to set them.
# - For Size, ensure it is an int > 10 (inches)
#   - If it is not, default to a 10" pizza (you can store ten). These checks should occur in init as well.
# - For toppings, you will need to add the toppings.
#   - This method needs to be able to handle multiple values.
#   - Append all elements to the list.
# Create a method that returns the amount of toppings.
# In your __init__() method, you should take in size and sauce as parameters.
# - Sauce should have a default value of red.
# - Size will not have a default value; use the parameter with the same safety checks defined above (you can use the set method).
# Within __init__(), you will need to:
# - Assign the parameter for size to a size attribute.
# - Assign the parameter for sauce to the attribute.
# - Create the toppings attribute, starting off as a list only holding cheese.


# You will be creating a Pizzeria class with the following attributes:
# - orders, the number of orders placed. Should start at 0.
# - price_per_topping, a static value for the price per topping of 0.30.
# - price_per_inch, a static value of 0.60 to denote how much the pizza cost per inch of diameter.
# - pizzas, a list of all the pizzas with the last ordered being the last in the list.
# You will need the following methods:
# - __init__()
#   - This one does not need to take in any extra parameters.
#   - It should create and set the attributes defined above.
# - placeOrder():
#   - This method will allow a customer to order a pizza.
#     - Which will increment the number of orders.
#   - It will need to create a pizza object.
#   - You will need to prompt the user for:
#     - the size
#     - the sauce, tell the user if nothing is entered it will default to red sauce (check for an empty string).
#     - all the toppings the user wants, ending prompting on an empty string.
#     - Implementation of this is left to you; you can, for example:
#       - have a while loop and append new entries to a list
#       - have the user separate all toppings by a space and turn that into a list.
#   - Upon completion, create the pizza object and store it in the list.
# - getPrice()
#   - You will need to determine the price of the pizza.
#   - This will be (pizza.getSize() * price_per_inch) + pizza.getAmountOfToppings() * price_per_topping.
#   - You will have to retrieve the pizza from the pizza list.
# - getReceipt()
#   - Creates a receipt of the current pizza.
#   - Show the sauce, size, and toppings.
#   - Show the price for the size.
#   - The price for the toppings.
#   - The total price.
# - getNumberOfOrders()
#   - This will simply return the number of orders.


# - Declare your pizzeria object.
# - Enter a while loop to ask if the user wants to order a pizza.
# - Exit on the word `exit`.
# - Call the placeOrder() method with your class instance.
# - After the order is placed, call the getReceipt() method.
# - Repeat the loop as needed.
# - AFTER the loop, print how many orders were placed.


# Example output:
"""
Would you like to place an order? exit to exit
yes
Please enter the size of pizza, as a whole number. The smallest size is 10
20
What kind of sauce would you like?
Leave blank for red sauce
garlic
Please enter the toppings you would like, leave blank when done
pepperoni
bacon

You ordered a 20" pizza with garlic sauce and the following toppings:
                                                                  cheese
                                                                  pepperoni
                                                                  bacon
You ordered a 20" pizza for 12.0
You had 3 topping(s) for $0.8999999999999999
Your total price is $12.9

Would you like to place an order? exit to exit
"""
class Pizza:
  def __init__(self, size, sauce = "red"):
    self.setSize(size)
    self.sauce = sauce
    self.toppings = ['cheese']

  def getToppings(self):
    return self.toppings

  def setSize(self, size):
    if size > 10:
      self.size = size
    else:
      self.size = 10
    
  def getSize(self):
    return self.size

  def setToppings(self, *toppings):
    for topping in toppings:
      self.toppings.append(topping)
    
  def amountTopping(self):
    return len(self.toppings)

        

class Pizzaria:
  topping_price = 0.30
  size_price = 0.60

  def __init__(self):
    self.orders = 0
    self.pizza = []

  def placeOrder(self):
    self.orders += 1

    size = int(input('Enter the Pizza size in inches:'))
    sauce = input('Enter type of Sauce(leave blank for red):')
    if sauce == '':
      sauce = 'red'
    input_toppings = input('Enter toppings and seperate with spaces')
    toppings = input_toppings.split() if input_toppings else []
    pizza = Pizza(size, sauce)
    pizza.setToppings(*toppings)
    self.pizza.append(pizza)
    self.getReceipt(pizza)
  def getPrice(self, pizza):
    size_Price = pizza.getSize() * Pizzaria.size_price
    topping_Price = pizza.amountTopping() * Pizzaria.topping_price
    total_price = size_Price + topping_Price
    return total_price
  def getReceipt(self, pizza):
    print("\n---Receipt---")
    print(f"Sauce:{pizza.sauce}")
    print(f"Size:{pizza.getSize()} inches")
    print(f"Toppings: {', '.join(pizza.getToppings())}")
    print(f"Price for size:${pizza.getSize() * Pizzaria.size_price:.2f}")
    print(f"Price for toppings:${pizza.amountTopping() * Pizzaria.topping_price:.2f}")
    print(f"Total:${self.getPrice(pizza):.2f}\n")
  def get_orders(self):
    return self.orders
  
def main():
  pizzaria = Pizzaria()

  while(True):
    order = input("Place an order?(type 'exit' to quit)")
    if order.lower() == 'exit':
      break
    else:
      pizzaria.placeOrder()
  print(f"Total number of orders placed {pizzaria.get_orders()}")
if __name__ == "__main__":
  main()