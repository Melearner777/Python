# Program to print the given pattern

# Input: Get the number of rows from the user
rows = int(input("Enter the number of rows: "))

# Loop through each row
for i in range(1, rows + 1):
    # Loop through each column in the current row
    for j in range(1, i + 1):
        print("*", end=" ")
    # Move to the next line after printing each row
    print()

