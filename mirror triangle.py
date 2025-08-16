rows = 5 

for i in range(1, rows + 1):

    # Print spaces
    for j in range(rows - i):
        print(" ", end="")

    # Print stars
    for k in range(i):
        print("*", end="")

    print()
