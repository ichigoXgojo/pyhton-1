def factorial(x):
    '''this is a rescrusive function to find the factorial of an integer'''
    if x == 0 or x == 1:
        return1
    else:

        return x * factorial(x - 1)

print(factorial.__doc__)
print("The factorial of 1:", factorial(1))
print("The factorial of 2:", factorial(2))
print("The factorial of 3:", factorial(3))
print("The factorial of 4:", factorial(4))