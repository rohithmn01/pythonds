from itertools import combinations
nums=[3,1,4,2]
comb=[]
for x,y in combinations(range(len(nums)+1), r=2):
    if len(nums[x:y]) == 3:
        comb.append(nums[x:y])

print(comb)

flag=0
for lis in comb:
    for i,x in enumerate(lis):
        for j,y in enumerate(lis):
            for k,z in enumerate(lis):
                if i < j < k and x < z < y:
                    flag=1
if flag == 1:
    print("True")
else:
    print("Fasle")
