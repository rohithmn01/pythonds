class Solution:
    def isAnagram(self,s1,s2) -> bool:
        flag = 0
        if len(s1) != len(s2):
            return False
        for i in s1:
            if s1.count(i) != s2.count(i):
                flag=1
        if flag == 1:
            return False
        else:
            return True

    def groupAnagrams(self,lis):
        final_lis = []
        for i in range(len(lis)):
            sub_list=[]
            for j in range(i+1, len(lis)):
                res = self.isAnagram(lis[i],lis[j]) 
                print(lis[i])
                print(lis[j])
                print(res)   
                print("-----------")
                if res:
                    sub_list.append(lis[j])
                    lis.remove(lis[j])
            sub_list.append(lis[i])
            lis.remove(lis[i])
            final_lis.append(sub_list)

        return final_lis

    def groupAnagramsNEW(self,lis):
        final_lis = []
        lis2 = lis.copy()
        for i in lis2:
            sub_list=[]
            print(i)
            print(f"before remove {lis2}")
            for j in lis2:
                if i == j:
                    continue
                res = self.isAnagram(i,j)
                if res:
                    sub_list.append(j)
                    lis2.remove(j)
            sub_list.append(i)
            lis2.remove(i)
            final_lis.append(sub_list)
            print(f"after remove {lis2}")
        return final_lis


    def groupAnagramsSort(self,lis):
        dis = {}
        for i in lis:
            s = ''.join(sorted(list(i)))
            print(s)
            dis[i]=s
        print(dis.keys())
        print(set(dis.values()))
        #for k,v in dis.items():
        res={}
        for k in dis.keys():
            for n in set(dis.values()):
                if dis[k] == n:
                    if n not in res:
                        res[n]=[k]
                    else:
                        res[n].append(k)

        print(res)

    def groupAnagramsSort2(self,lis):
        dis = {}
        new_lis=[]
        for i in lis:
            s = ''.join(sorted(list(i)))
            print(s)
            if s not in dis:
                dis[s]=[i]
            else:
                dis[s].append(i)
        print(dis)
        for v in dis.values():
            new_lis.append(v)
        print(new_lis)

        #return list(dis.values())
        return [v for v in dis.values()]

obj = Solution()
result = obj.groupAnagramsSort2(["eat","tea","tan","ate","nat","bat"])

print(result)

# d = {n:[k for k in files.keys() if files[k] == n] for n in set(files.values())}