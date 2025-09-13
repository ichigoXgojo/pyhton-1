import math

def calculate_trigonometric_values(degrees):
    """
    Calculates the sine, cosine, and tangent of an angle given in degrees.

    Args:
        degrees (float): The angle in degrees.

    Returns:
        A tuple containing the sine, cosine, and tangent values.
    """
    
    radians = math.radians(degrees)
    sin_value = math.sin(radians)
    cos_value = math.cos(radians)
    tan_value = math.tan(radians)

    return sin_value, cos_value, tan_value

if __name__ == "__main__":
    try:
        
        user_input = input("Enter the angle in degrees: ")

        angle_in_degrees = float(user_input)

        sine, cosine, tangent = calculate_trigonometric_values(angle_in_degrees)

        print(f"\nFor an angle of {angle_in_degrees} degrees:")
        print(f"Sine: {sine:.4f}")
        print(f"Cosine: {cosine:.4f}")
        print(f"Tangent: {tangent:.4f}")

    except ValueError:
        
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        
        print(f"An error occurred: {e}")
