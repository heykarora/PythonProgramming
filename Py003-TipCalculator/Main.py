# Tip Calculator
# This program calculates the total bill after adding a tip
# and divides the amount equally among all the people.

# Display a welcome message.
print("Welcome to tip calculator!")

# Ask the user to enter the total bill amount.
# Convert the input into a floating-point number to allow decimals.
totalBill = float(input("Enter the total bill amount :\n"))

# Ask the user to enter the tip percentage they want to leave.
# Convert the input into an integer.
tip2Give = int(input("How much tip would you like to leave (10, 12, 15):\n"))

# Ask how many people will split the bill.
# Convert the input into an integer.
totalPeople = int(input("Among how many people to split the bill? :\n"))

# Calculate the bill after adding the selected tip percentage.
bill = totalBill+(totalBill*tip2Give/100)

# Divide the bill equally among all the people.
finalBill = bill/totalPeople

# Display the amount each person needs to pay.
print(finalBill)
