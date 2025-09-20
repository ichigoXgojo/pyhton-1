test_dict = {'codingal': 2, 'is': 2, 'best': 2, 'for': 2, 'you': 1}

print("the original dictionary is : " + str(test_dict))

k = 2

res = 0
for key, val in test_dict.items():
    if test_dict[key] == k:
        res = res + 1

print("frequency of k is : " + str(res))