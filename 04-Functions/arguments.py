def add(*args):
    sum=0
    for i in args:
        sum = sum + i
    return sum

res = add(1,2,3,4)
print(res)


def printKWArgs(**kwargs):
    print(kwargs)

printKWArgs(server='localhost', port=3306, user='root', password='xxxxxxxxxxxxx')
#Note: Always place **kwargs at the end of the function