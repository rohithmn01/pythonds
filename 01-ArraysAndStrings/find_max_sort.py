b="12166666666666888888823"
a=[]
for i in b:
    if b.count(i) == 1:
        a.append(i)
    elif i not in a:
        a.append(i)

for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j]=temp

print(a)