# Write a Python program that takes a list of numbers (input by the user) and finds the maximum value in that list.

# Step 1: Ask the user to input a list of numbers (separated by spaces)
user_input = "1 3 5 9 4 7 8"

# Step 2: Split the input string into a list of numbers
numbers = user_input.split()

# Step 3: Convert the list of strings into integers
numbers = [int(num) for num in numbers]

# Step 4: Find the maximum number in the list
max_number = max(numbers)

# Step 5: Display the result
print(f"The maximum number in the list is: {max_number}")