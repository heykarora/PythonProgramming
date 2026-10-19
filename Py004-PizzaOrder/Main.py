# Py Pizza Order
# This program takes a pizza order, calculates the price based on
# the pizza size and selected toppings, and displays the total bill.

# Display a welcome message to the customer.
print("Welcome to PyPizza, please state your order!")

# Ask the customer to choose a pizza size.
# Convert the input to lowercase so uppercase and lowercase answers work.
pizzaSize = input("What size would you like? (S, M, L) :\n").lower()

# Ask whether the customer wants pepperoni.
# Convert the input to lowercase for consistent comparisons.
addPepporoni = input("Would you like pepporoni in your pizza? (y/n)\n").lower()

# Ask whether the customer wants extra cheese.
# Convert the input to lowercase for consistent comparisons.
extraCheese = input("Would you like extra cheese? (y/n) :\n").lower()

# Initialize the bill to zero before adding the selected items.
bill = 0

# Add the base price according to the selected pizza size.
# Small pizza costs 15.
if pizzaSize == "s":
    bill += 15

# Medium pizza costs 20.
elif pizzaSize == "m":
    bill += 20

# Large pizza costs 25.
elif pizzaSize == "l":
    bill += 25

# Add the pepperoni price if the customer selects "y".
if addPepporoni == "y":

    # Pepperoni costs 2 extra for a small pizza.
    if pizzaSize == "s":
        bill += 2

    # Pepperoni costs 3 extra for a medium or large pizza.
    else:
        bill += 3

# Add 1 to the bill if the customer wants extra cheese.
if extraCheese == "y":
    bill += 1

# Display the final bill after calculating all selected options.
print(f"Your total bill is :\n{bill}")
