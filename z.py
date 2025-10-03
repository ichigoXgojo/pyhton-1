s1 = ['x', 'y', 'z'] 
s2 = {'b', 'a', 'c'}
s3 = list(zip(s1, s2))
print(s3,"\n")

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]  

for x, y in zip(list1, list2[::-1]):
    print(x, y)


stocks = ['playstation', 'nitendo', 'xbox', 'Koenigsegg']
prices = ['1,000,000', '500,000', '300,000,000', '900,000,000,000,000,000']

new_dict = {stock: price for stock, price in zip(stocks, prices)}

print('\n{}'.format(new_dict))
