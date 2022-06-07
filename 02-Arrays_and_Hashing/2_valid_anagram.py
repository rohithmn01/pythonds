class Solution:
    def isAnagram(self,s1:str, s2:str) -> bool:
        flag=0
        if len(s1) != len(s2):
            return False
        else:
            for i in s1:
                if s1.count(i) != s2.count(i):
                    flag=1

        if flag == 1:
            return False
        else:
            return True
obj = Solution()
res = obj.isAnagram("rohith","kavya")
print(res)