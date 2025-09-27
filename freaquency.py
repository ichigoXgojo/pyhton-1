def check_value_frequency(test_dict, target_value):
    """
    Checks the frequency (count) of a specific value within the values
    of a given dictionary.

    Args:
        test_dict (dict): The dictionary to search within.
        target_value: The value whose frequency needs to be counted.

    Returns:
        int: The number of times the target_value appears in the
             dictionary's values.
    """
    frequency_count = 0
    
    # Iterate through all the values of the dictionary
    for value in test_dict.values():
        if value == target_value:
            frequency_count += 1
            
    return frequency_count

# --- Example Usage ---

# 1. Define the test dictionary
# Note: The keys are unique, but the values can be repeated.
test_dictionary = {
    'A': 'apple',
    'B': 'banana',
    'C': 100,
    'D': 'apple',
    'E': 'grape',
    'F': 100,
    'G': 'apple',
    'H': 50
}

print(f"Test Dictionary: {test_dictionary}")
print("-" * 30)

# 2. Check the frequency for different values

# Target 1: 'apple' (Expected count: 3)
target_value_1 = 'apple'
count_1 = check_value_frequency(test_dictionary, target_value_1)
print(f"Frequency of '{target_value_1}': {count_1}")

# Target 2: 100 (Expected count: 2)
target_value_2 = 100
count_2 = check_value_frequency(test_dictionary, target_value_2)
print(f"Frequency of {target_value_2}: {count_2}")

# Target 3: 'mango' (Expected count: 0)
target_value_3 = 'mango'
count_3 = check_value_frequency(test_dictionary, target_value_3)
print(f"Frequency of '{target_value_3}': {count_3}")

# Target 4: 50 (Expected count: 1)
target_value_4 = 50
count_4 = check_value_frequency(test_dictionary, target_value_4)
print(f"Frequency of {target_value_4}: {count_4}")

# Alternative method using list comprehension (more concise):
def check_frequency_concise(d, v):
    return sum(1 for val in d.values() if val == v)

print("-" * 30)
print(f"Concise method check for 'banana': {check_frequency_concise(test_dictionary, 'banana')}")
