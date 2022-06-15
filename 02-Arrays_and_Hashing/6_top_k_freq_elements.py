from collections import Counter
class Solution:
    def topElements(self,lis,k):
        di = dict(Counter(lis))
        print(di)
        count = 0
        for i,v in di.items():
            if count < k:
                print(di[v])
                count +=1

    def topElementsNew(self,lis,k):
        d={}
        for i in lis:
            if i not in d:
                d[i] = lis.count(i)
        print(d)

obj = Solution()
res = obj.topElementsNew([1,1,1,2,2,3],2)
print(res)

