# Python program to print elements at odd positions in a list
import sys

def print_odd_position_elements(input_list):
    # Iterate through the list and print elements at odd positions
    for i in range(1, len(input_list), 2):
        print(input_list[i])

# Check if the script is run with command line arguments
if len(sys.argv) > 1:
    # Convert command line arguments to a list of integers
    input_list = [int(arg) for arg in sys.argv[1:]]
    
    # Print elements at odd positions in the list
    print("Elements at odd positions:")
    print_odd_position_elements(input_list)

else:
    print("Please provide a list of integers as command line arguments.")

