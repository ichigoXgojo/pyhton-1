def find_symmetric_difference(set_a, set_b):
    """
    Calculates the symmetric difference between two sets.

    The symmetric difference of two sets A and B is the set of elements
    which are in either of the sets, but not in their intersection.
    Mathematically, it is (A \ B) U (B \ A).

    Args:
        set_a (set): The first set.
        set_b (set): The second set.

    Returns:
        set: A new set containing the symmetric difference.
    """
    # Python's built-in symmetric_difference() method is the most efficient way.
    # Alternatively, the ^ operator can be used: set_a ^ set_b
    symmetric_diff = set_a.symmetric_difference(set_b)
    return symmetric_diff

# --- Example Usage ---

# 1. Define the input sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")

# 2. Calculate the symmetric difference
result_set = find_symmetric_difference(set1, set2)

# 3. Print the result
print("\n--- Result ---")
print(f"The symmetric difference is: {result_set}")

# Verification:
# Elements unique to Set 1: {1, 2, 3}
# Elements unique to Set 2: {6, 7, 8}
# Symmetric Difference (Union of unique elements): {1, 2, 3, 6, 7, 8}

# Example using the caret (^) operator for comparison
print(f"\nVerification using the '^' operator: {set1 ^ set2}")
