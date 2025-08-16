rows = int(input("please enter the total number of rows : "))
number = 1 #initialize by 1

print("Floyd's triangle")

for i in range(1, rows + 1):

    for j in range(i):
        print(number, end=' ')
        number += 1
    print()