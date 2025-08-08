import math

def find_square_root(number):
  """
  Calculates the square root of a number.

  Args:
    number: A positive number.

  Returns:
    The square root of the number.
  """
  if number < 0:
    return "Error: Cannot calculate the square root of a negative number."
  else:
    return math.sqrt(number)

# Example usage
num = 16
square_root = find_square_root(num)
print(f"The square root of {num} is {square_root}") 