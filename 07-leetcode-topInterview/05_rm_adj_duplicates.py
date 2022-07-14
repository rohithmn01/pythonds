from collections import OrderedDict
stg="yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy"
k=4
def rm_dup(stg,k):

    dic=OrderedDict()
    for i in stg:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] +=1 
            if dic[i] == k:
                dic.pop(i)
    print(dic)
    res=""
    for k,v in dic.items():
        res = res + k*v
    print(res)
rm_dup(stg,k)
# def rm_dup2():
#     stk=[]
#     for i in stg:
#         if not stk or i not in stk[0]





