binary = input("Enter the bin number: ")
lis = list(binary)
deci = []
count=0
for i in range(len(lis)-1, -1, -1):
    res = pow(2,0+count)
    count = count + 1
    if lis[i] == '1':
        deci.append(res)

res=0
for j in deci:
    res = res + j

print(f"Decimal Number of {binary} is : {res}")