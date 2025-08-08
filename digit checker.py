# Get input from the user
number_str = input("Enter a number: ")

# Check if the input is a valid digit string
if number_str.isdigit():
  # Count the number of digits
  num_digits = len(number_str)
  
  # Print the result
  print(f"The number of digits in {number_str} is: {num_digits}")
else:
  print("Invalid input. Please enter a valid number.")
