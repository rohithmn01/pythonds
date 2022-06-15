def threeSum(lis):
    res=[]
    for i,x in enumerate(lis):
        for j,y in enumerate(lis):
            for k,z in enumerate(lis):
                if i == j or j == k or i == k:
                    continue
                if x + y + z == 0:
                    res.append([x,y,z])
    #print(res)
    for l in res:
        l.sort()
    new_res=[]
    for r in res:
        if r not in new_res:
            new_res.append(r)
    print(new_res)



res=threeSum([-1,0,1,2,-1,-4])
print(res)