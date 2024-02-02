def binary_to_hex(binary_string):
    hex_string = hex(int(binary_string, 2))[2:]
    return hex_string.upper()

def main():
    binary_string = input("Enter a binary number: ")

    # Convert and print the hexadecimal equivalent
    hex_string = binary_to_hex(binary_string)
    print(f"Hexadecimal equivalent: {hex_string}")

if __name__ == "__main__":
    main()
