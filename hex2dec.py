def hex_to_decimal(hex_string):
    decimal = 0
    length = len(hex_string)

    # Iterate through each character in the hexadecimal string
    for i in range(length):
        digit = 0

        # Convert hexadecimal digit to decimal
        if '0' <= hex_string[i] <= '9':
            digit = int(hex_string[i])
        elif 'A' <= hex_string[i] <= 'F':
            digit = ord(hex_string[i]) - ord('A') + 10
        elif 'a' <= hex_string[i] <= 'f':
            digit = ord(hex_string[i]) - ord('a') + 10
        else:
            print(f"Invalid hexadecimal digit '{hex_string[i]}'")
            exit(1)

        # Update the decimal value
        decimal += digit * (16 ** (length - i - 1))

    return decimal

def main():
    hex_string = input("Enter a hexadecimal number: ")

    # Convert and print the decimal equivalent
    decimal = hex_to_decimal(hex_string)
    print(f"Decimal equivalent: {decimal}")

if __name__ == "__main__":
    main()
