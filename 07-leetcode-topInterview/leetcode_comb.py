from operator import itemgetter
s=[5,2,3,7]
e=[7,2,4,8]
res=[]
for i in s:
    for j in e:
        res.append([i,j])
        e.remove(j)
        break
print(res)
sor_res=sorted(res,key=itemgetter(0))
print(sor_res)

for i,v in sor_res:
    if v[1] < 