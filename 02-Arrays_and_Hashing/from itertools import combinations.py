from itertools import combinations

a=[2,3,5]
c=[]
for x,y in combinations(range(len(a)+1), r=2):
    c.append(a[x:y])

print(c)


