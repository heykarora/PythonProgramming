# Band Name Generator
# This program creates a band name using the user's city of origin
# and the name of their first pet.

# Display a welcome message to the user.
print("Welcome to Band Name Generator!")

# Ask the user to enter the name of their city of origin.
# The input is stored in the variable cityName.
cityName = input("Enter the city name of your origin :\n")

# Ask the user to enter the name of their first pet.
# The input is stored in the variable petName.
petName = input("Enter your first pet name :\n")

# Combine the city name and pet name to generate a band name.
# An f-string inserts both variable values into the output.
print(f"Your bane name should be :\n{cityName} {petName}")
