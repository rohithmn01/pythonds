def twoSum2(lis,t):
    for i,v in enumerate(lis):
        for j,g in enumerate(lis):
            if i == j:
                continue
            if v + g == t:
                print(i)
                print(j)
                break
        break

twoSum2([2,3,4],6)