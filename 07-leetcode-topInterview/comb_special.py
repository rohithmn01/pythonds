from itertools import combinations
comb=[]
res=[]
def substrCount(n, s):
    for x,y in combinations(range(len(s)+1),2):
        comb.append(s[x:y])
    #print(comb)
    for i in comb:
        if len(i) == 1:
            res.append(i)
        elif len(i) == 2 and len(set(i)) == 1:
            res.append(i)
        elif len(i) > 2:
            mid = len(i)//2
            l = list(i)
            l.pop(mid)
            if len(set(l)) == 1:
                res.append(i)
    #print(res)
    return len(res)
substrCount(5,"aaaa")