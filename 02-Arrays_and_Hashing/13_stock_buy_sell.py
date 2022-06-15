def stockBuySell(lis):
    rem_lis=[]
    min_no = sorted(lis)[0]
    #print(min_no)
    i = lis.index(min_no)
    #print(i)
    for j in range(i,len(lis)):
        rem_lis.append(lis[j])
    #print(rem_lis)
    max_no=sorted(rem_lis)[len(rem_lis)-1]
    #print(max_no)
    return max_no - min_no


res = stockBuySell([7,6,4,3,1])
print(res)