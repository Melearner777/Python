# Sample string
my_string = "abcdefghijk"

# Accessing single characters using indexing
first_char = my_string[0]
second_char = my_string[1]

# Accessing a substring using slicing
substring_1 = my_string[2:6]  # Characters from index 2 to 5
substring_2 = my_string[:6]   # Characters from the beginning to index 5
substring_3 = my_string[6:]   # Characters from index 6 to the end

# Displaying the results
print(f"Original String: {my_string}")
print(f"First Character: {first_char}")
print(f"Second Character: {second_char}")
print(f"Substring [2:6]: {substring_1}")
print(f"Substring [:6]: {substring_2}")
print(f"Substring [6:]: {substring_3}")
