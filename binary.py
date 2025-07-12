def decimal_to_binary(n):
    """Convert a decimal number to binary."""
    return bin(n).replace("0b", "")

def binary_to_decimal(b):
    """Convert a binary string to decimal."""
    return int(b, 2)

def binary_addition(b1, b2):
    """Add two binary numbers."""
    return bin(int(b1, 2) + int(b2, 2)).replace("0b", "")

def binary_subtraction(b1, b2):
    """Subtract two binary numbers (b1 - b2)."""
    return bin(int(b1, 2) - int(b2, 2)).replace("0b", "")

# Example usage
if __name__ == "__main__":
    dec = 25
    bin_val = decimal_to_binary(dec)
    print(f"Decimal {dec} to Binary: {bin_val}")

    bin_num = "11001"
    dec_val = binary_to_decimal(bin_num)
    print(f"Binary {bin_num} to Decimal: {dec_val}")

    b1 = "1010"
    b2 = "110"
    print(f"Binary Addition: {b1} + {b2} = {binary_addition(b1, b2)}")
    print(f"Binary Subtraction: {b1} - {b2} = {binary_subtraction(b1, b2)}")




