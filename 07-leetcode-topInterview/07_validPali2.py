def pali(st):
    rev = []
    for i in range(len(st)-1,-1,-1):
        rev.append(st[i])
    if st == ''.join(rev):
        return True
    else:
        return False

def checkAll(inp):
    l = list(inp)
    for i in range(len(l)):
        l = list(inp)
        l.remove(l[i])
        print(''.join(l))
        res = pali(''.join(l))
        if res:
            return True 


inp = "madam"
r = pali(inp)
if not r:
    res = checkAll(inp)
else:
    print(True)


    