def octal_to_decimal(octal_string):
    decimal = int(octal_string, 8)
    return decimal

def main():
    octal_string = input("Enter an octal number: ")

    # Convert and print the decimal equivalent
    decimal = octal_to_decimal(octal_string)
    print(f"Decimal equivalent: {decimal}")

if __name__ == "__main__":
    main()
