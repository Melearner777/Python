def hex_to_binary(hex_string):
    binary_string = bin(int(hex_string, 16))[2:]
    return binary_string

def main():
    hex_string = input("Enter a hexadecimal number: ")

    # Convert and print the binary equivalent
    binary_string = hex_to_binary(hex_string)
    print(f"Binary equivalent: {binary_string}")

if __name__ == "__main__":
    main()
