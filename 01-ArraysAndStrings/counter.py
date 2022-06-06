from collections import Counter

my_lis = [1,1,1,3,4,5,5,6,7,3,2,1,1,5,6,4]
print(Counter(my_lis))
print(Counter(my_lis).keys())
print(Counter(my_lis).values())
print(Counter(my_lis).items())