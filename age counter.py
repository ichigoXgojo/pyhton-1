def check_age():
    """
    Prompts the user to enter their age, validates the input, and
    checks if the age is even or odd.
    """
    try:
        
        age_str = input("Please enter your age: ")
        age = int(age_str)

        
        if age < 0:
            print("Error: Age cannot be a negative number. Please enter a valid age.")
        elif age > 150: 
            print("Error: The age entered seems unusually high. Please enter a realistic age.")
        else:
            print(f"Your age is: {age}")
            
            if age % 2 == 0:
                print("Your age is an even number.")
                
            else:
                print("Your age is an odd number.")
    
    except ValueError:
        
        print("Error: Invalid input. Please enter a number for your age.")

if __name__ == "__main__":
    check_age()
