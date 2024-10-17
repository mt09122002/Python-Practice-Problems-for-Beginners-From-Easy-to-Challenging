# Write a Python program that asks the user to input a list of numbers (separated by spaces) and calculates the sum of all the numbers.

# Step 1: Ask the user to input a list of numbers (separated by spaces)
user_input = "1 3 5 6 4 7 8"

# Step 2: Split the input string into a list of numbers
numbers = user_input.split()

# Step 3: Convert the list of strings into integers
numbers = [int(num) for num in numbers]

# Step 4: Calculate the sum of the numbers
total_sum = sum(numbers)

# Step 5: Display the result
print(f"The sum of the numbers is: {total_sum}")