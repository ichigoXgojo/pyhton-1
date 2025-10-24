import math

class Circle:
    """
    A class used to represent a Circle, constructed by its radius.

    It provides methods to compute the area and the perimeter (circumference)
    of the circle.
    """

    def __init__(self, radius):
        """
        Constructor for the Circle class.

        Args:
            radius (float or int): The radius of the circle.
        """
        # Ensure the radius is non-negative
        if radius < 0:
            raise ValueError("Radius must be a non-negative number.")
        self.radius = radius

    def compute_area(self):
        """
        Computes the area of the circle using the formula: Area = pi * r^2.

        Returns:
            float: The area of the circle.
        """
        # Area formula: π * r^2
        return math.pi * (self.radius ** 2)

    def compute_perimeter(self):
        """
        Computes the perimeter (circumference) of the circle using the formula:
        Perimeter = 2 * pi * r.

        Returns:
            float: The perimeter of the circle.
        """
        # Perimeter (Circumference) formula: 2 * π * r
        return 2 * math.pi * self.radius

# --- Demonstration ---
if __name__ == "__main__":
    # Create a new Circle object with a radius of 5.0
    radius_value = 5.0
    try:
        my_circle = Circle(radius_value)

        # Calculate and print the results
        area = my_circle.compute_area()
        perimeter = my_circle.compute_perimeter()

        print(f"--- Circle Calculation Results ---")
        print(f"Radius (r): {my_circle.radius}")
        print(f"Area (A = \pi r^2): {area:.4f}")
        print(f"Perimeter (P = 2\pi r): {perimeter:.4f}")

        # Example with a different radius
        second_circle = Circle(12)
        print("\n--- Second Circle (Radius 12) ---")
        print(f"Area: {second_circle.compute_area():.4f}")
        print(f"Perimeter: {second_circle.compute_perimeter():.4f}")

    except ValueError as e:
        print(f"Error creating circle: {e}")

    # Displaying the formulas (using LaTeX notation for clarity)
    print("\n--- Formulas Used (More on Object-Oriented Programming) ---")
    print("The power of OOP is that the data (radius) and the functions (methods) that operate on it are bundled together in the 'Circle' object.")
    print(f"Area Formula: $A = \pi r^2$")
    print(f"Perimeter Formula: $P = 2 \pi r$")
