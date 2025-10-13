"""
Dog Class Example demonstrating Class and Instance Variables.
"""

class Dog:
    # 1. Class Variable: Shared by all instances of the Dog class.
    # We'll use 'species' as the shared characteristic.
    species = "Canis familiaris"

    def __init__(self, name, breed):
        # 2. Instance Variables: Unique to each instance (dog object).
        # 'name' and 'breed' will be our two instance variables.
        self.name = name
        self.breed = breed
        # Adding a third instance variable for more context (age)
        self.age = 0 # Initialized age, can be updated later

    def set_age(self, age):
        """Sets the age of the dog instance."""
        if age >= 0:
            self.age = age

    def display_details(self):
        """Displays all details for the dog instance."""
        print("-" * 30)
        print(f"Dog Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Age: {self.age} years")
        # Accessing the shared class variable
        print(f"Species (Class Variable): {Dog.species}")
        print("-" * 30)


# --- Program Execution ---

# 1. Create the first Dog object (Golden Retriever)
dog1 = Dog(name="Buddy", breed="Golden Retriever")
dog1.set_age(5)

# 2. Create the second Dog object (Siberian Husky)
dog2 = Dog(name="Ghost", breed="Siberian Husky")
dog2.set_age(3)

print("--- Displaying Dog Details ---")

# Display details for the first dog
dog1.display_details()


# Display details for the second dog
dog2.display_details()


# Demonstration of the Class Variable:
print("\n--- Class Variable Demonstration ---")
print(f"The shared species for all dogs is: {Dog.species}")

# We can also access the class variable via an instance, but it's cleaner
# to use the class name (Dog.species) for accessing it.
print(f"Buddy's species (via instance): {dog1.species}")

# Changing the class variable affects all instances
Dog.species = "Domestic Dog"
print(f"\n*Species updated globally to: {Dog.species}*")
print(f"Ghost's updated species: {dog2.species}")
