class Solution:
    def countRep(self,path:str) -> dict:
        dic={}
        with open(path) as f:
            while True:
                line = f.readline()
                if not line:
                    break
                lis = line.split()
                for i in lis:
                    if i not in dic:
                        #dic[i] = lis.count(i) + dic.get(i,0)
                        dic[i] = lis.count(i)
        return dic
    def countRep2(self,path:str) -> dict:
        dic={}
        with open(path) as f:
            for line in f:
                for word in line.split():
                    if word in dic:
                        dic[word]+=1
                    else:
                        dic[word]=1
        return dic
                    


obj = Solution()
res = obj.countRep2("/Users/i346327/pythonds/pythonds/03-FileHandling/file1.txt")
print(res)


#
# check if file exists or not
# 

import os.path
os.path.exists("/Users/i346327/pythonds/pythonds/03-FileHandling/file1.txt")
