import itertools
s = "110011000"
k=2

l = list(itertools.product([0,1],repeat=k))
lis = [''.join(list(map(str,i))) for i in l]
print(lis)


comb=[]
for x,y in itertools.combinations(range(len(s)+1),r=2):
    if len(s[x:y]) == k:
        comb.append(s[x:y])

print(comb)

flag=0
for i in lis:
    if i not in comb:
        flag=1

if flag == 1:
    print("False")
else:
    print("True")


