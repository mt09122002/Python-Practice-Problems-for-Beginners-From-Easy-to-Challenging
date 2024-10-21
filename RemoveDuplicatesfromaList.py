# Write a Python program that removes any duplicate numbers from a list of numbers (separated by spaces)

# Step 1: The list of numbers
user_input = "1 2 3 4 5 6 7 8 9 0"

# Step 2: Split the input string into a list of numbers
numbers = user_input.split()

# Step 3: Convert the list of strings into integers
numbers = [int(num) for num in numbers]

# Step 4: Remove duplicates by converting the list to a set, then back to a list
unique_numbers = list(set(numbers))

# Step 5: Display the list with duplicates removed
print(f"The list with duplicates removed is: {unique_numbers}")
