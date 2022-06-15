from itertools import permutations, combinations
def longSubStr(s):
    comb=[]
    dic={}
    for x,y in combinations(range(len(s)+1),r=2):
        comb.append(s[x:y])

    for i in comb:
        if len(i) == len(set(i)):
            dic[i] = len(i)
            
    print(dic)
    max=0
    for k,v in dic.items():
        if v > max:
            max=v

    key_list = list(dic.keys())
    value_list = list(dic.values())
    ind = value_list.index(max)
    return key_list[ind]


res=longSubStr("pwwkew")
print(res)