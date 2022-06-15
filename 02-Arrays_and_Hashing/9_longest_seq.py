def longSeq(lis):
    a = list(set(lis))
    a.sort()
    print(a)
    res=[]
    for i in range(len(a)):
        if len(a)-1 == i: 
            if a[i] - a[i-1] > 1:
                break
            else:
                res.append(a[i])
                break
            
        if a[i+1] - a[i] > 1 and a[i] - a[i-1] > 1:
            break
        res.append(a[i])
    return list(set(res))



res = longSeq([9,1,4,7,3,-1,0,5,8,-1,6])
print(res)