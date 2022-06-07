class Solution:
    def isAnagram(self, s1:str, s2:str) -> bool:
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


    def countAnagram(self, s:str) -> int:
        count=0
        l = s.split()
        for i in range(len(l)):
            for j in range(i+1, len(l)):
                res = self.isAnagram(l[i],l[j])
                if res:
                    count = count + 1
                    print(f"Anagrams are : {l[i]} and {l[j]}")
        return count

obj = Solution()
result = obj.countAnagram("rohith has three friends named - throhi cena and reeth")
print("################")
print(f"Count: {result}")
print("################")