class Solution:
    def romanToInt(self, s: str) -> int:
       dict = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
        } 
       s = s.replace("IV","IIII").replace("IX","VIIII")
       s = s.replace("XL","XXXX").replace("XC","LXXXX")
       s = s.replace("CD","CCCC").replace("CM","DCCCC")
      
       result = 0
       for i in range(len(s)):
           result += dict[s[i]];          


       return (result)
obj = Solution()
res = obj.romanToInt("IVIX")
print(res)