test_tup = (30, 2,3,4,9,8)
print("The original tuple is :" + str(test_tup))
K = 2
test_tup = list(test_tup)
temp = sorted(test_tup)
res = tuple(temp[:K] + temp[-K:])

print("The extracted values : " + str(res))
