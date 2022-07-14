def baseGame(ops):
    stk = []
    for i,v in enumerate(ops):
        #print(f"{i},{v}")
        if v == "C":
            stk.remove(stk[len(stk)-1])
        elif v == "D":
            stk.append(int(stk[len(stk)-1])*2)
        elif v == "+":
            stk.append(int(stk[len(stk)-1]) + int(stk[len(stk)-2]))
        else:
            stk.append(v)
    #print(stk)
    stk_int = list(map(int, stk))
    #print(stk_int)
    return sum(stk_int)


res = baseGame(["5","2","C","D","+"])
print(res)