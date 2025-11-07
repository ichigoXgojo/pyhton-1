class RomanConverter:
    """
    A class to convert integers (1 to 3999) to Roman numerals.
    Demonstrates encapsulation by holding the conversion map internally.
    """

    # Private class attribute (conventionally marked with _) to store the conversion pairs.
    # This map is ordered from largest to smallest value for the greedy algorithm.
    _roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    def __init__(self):
        """
        Initializes the RomanConverter object.
        """
        # The constructor adheres to OOP structure, even if no complex state is needed.
        pass

    def to_roman(self, num: int) -> str:
        """
        Converts a positive integer to its Roman numeral representation using 
        a greedy algorithm based on the encapsulated conversion map.

        Args:
            num: The integer (1 to 3999) to convert.

        Returns:
            The Roman numeral string.

        Raises:
            ValueError: If the input is not a valid integer within the supported range.
        """
        if not isinstance(num, int) or not (1 <= num <= 3999):
            raise ValueError("Input must be an integer between 1 and 3999.")

        result = ""
        temp_num = num

        # Iterate through the pre-defined map
        for value, symbol in RomanConverter._roman_map:
            # Repeatedly subtract the largest possible value and append its symbol
            while temp_num >= value:
                result += symbol
                temp_num -= value

        return result

# Example Usage demonstrating instantiation and method calling
if __name__ == "__main__":
    print("--- Roman Numeral Converter Demo ---")

    # Instantiation: Creating an object (instance) of the class
    converter = RomanConverter()

    # Test cases
    test_cases = [1994, 58, 4, 1, 3999, 145]

    for number in test_cases:
        try:
            # Method Invocation: Calling the to_roman method on the object instance
            roman_numeral = converter.to_roman(number)
            print(f"The integer {number} converts to: {roman_numeral}")
        except ValueError as e:
            print(f"Error converting {number}: {e}")

    # Test error handling for out-of-range inputs
    print("\n--- Error Handling Tests ---")
    try:
        converter.to_roman(5000)
    except ValueError as e:
        print(f"Attempting to convert 5000: {e}")

    try:
        converter.to_roman(0)
    except ValueError as e:
        print(f"Attempting to convert 0: {e}")