try:
    num1, num2 = eval(input("Enter two numbers separated by a comma: "))

    result = num1 / num2
    print("result is:", result)

except ZeroDivisionError:
    print("Error: Division by zero is error!!.")

except SyntaxError:
    print("Error: Please enter two numbers separated by a comma like this 1, 2.")

except:
    print("wrong input")

else:
    print("No exceptions")

finally:
    print("this will excecute no matter what")

