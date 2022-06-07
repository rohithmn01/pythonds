a=[8,1,1,8,2,3]
count=0
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] == a[j]:
            count=count+1
            print(a[i])
if count > 0:
    print("Contains Duplicates")
else:
    print("No Duplicates")
print(count)   