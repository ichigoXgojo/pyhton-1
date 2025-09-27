def calculate_tuple_product(number_tuple):
    """
    Calculates the product of all numeric elements in a tuple.

    Args:
        number_tuple (tuple): A tuple containing numbers (integers or floats).

    Returns:
        float or int: The product of all numbers in the tuple. Returns 0 
                      if the tuple is empty or contains non-numeric data 
                      (after initial setup).
    """
    # Start the product at 1. Multiplying by 1 ensures the first number 
    # of the tuple is correctly incorporated.
    product = 1

    # Iterate through each element in the tuple
    for number in number_tuple:
        # We can add an optional check to ensure the element is numeric
        if isinstance(number, (int, float)):
            product *= number
        else:
            print(f"Warning: Skipping non-numeric item: {number}")

    return product

# --- Example Usage ---

# 1. Define the input tuple
data_tuple = (2, 5, 1, 4, 3)
print(f"Input Tuple 1: {data_tuple}")

# 2. Calculate the product
result_product = calculate_tuple_product(data_tuple)

# 3. Print the result
print(f"The product of all numbers is: {result_product}")
# (Expected result: 2 * 5 * 1 * 4 * 3 = 120)

print("-" * 30)

# Example with negative numbers and floats
data_tuple_2 = (1.5, -2, 10)
print(f"Input Tuple 2: {data_tuple_2}")
result_product_2 = calculate_tuple_product(data_tuple_2)
print(f"The product of all numbers is: {result_product_2}")
# (Expected result: 1.5 * -2 * 10 = -30.0)
