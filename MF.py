numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
reasult = map(lambda x, y: x + y, numbers1, numbers2)
print(list(reasult))

nums = [1, 2, 3, 4, 5]
def sq(n):
    return n * n
square = list(map(sq, nums))
print("square of numbers in list")
print(square)