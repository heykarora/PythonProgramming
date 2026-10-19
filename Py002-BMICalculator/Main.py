
# BMI Calculator
# This program calculates the user's Body Mass Index (BMI)
# using their weight in kilograms and height in meters.

# Display a welcome message.
print("Welcome to BMI Calculator!")

# Ask the user to enter their weight in kilograms.
# Convert the input from a string to a floating-point number.
userWeigh = float(input("Enter your weight (in kgs.) :\n"))

# Ask the user to enter their height in meters.
# Convert the input from a string to a floating-point number.
userHeight = float(input("Enter your height (in meters) : \n"))

# Calculate BMI using the formula:
# BMI = weight / (height squared)
userBMI = userWeigh/(userHeight**2)

# Display the calculated BMI.
print(userBMI)

# Check the BMI value and display the corresponding category.
# A BMI below 18.5 is classified as underweight.
if userBMI < 18.5:
    print("You are underweight!")

# A BMI above 25 is classified as overweight in this program.
elif userBMI > 25:
    print("You are overweight!")

# All remaining BMI values are classified as normal weight.
else:
    print("You have normal weight!")
