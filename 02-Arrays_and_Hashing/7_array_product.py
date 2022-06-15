class Solution:
    def arrayProduct(self,lis):
        new_arr=[]
        for i,x in enumerate(lis):
            p=1
            for j,v in enumerate(lis):
                print(f"{p} and {j} ------- {i} and {j}")
                if i == j:   ####compare index and then continue
                    continue
                
                p = p * v
            new_arr.append(p)
        return new_arr

obj = Solution()
res = obj.arrayProduct([0,0])
print(res)