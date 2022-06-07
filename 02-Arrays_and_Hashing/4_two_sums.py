## Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
## Input: nums = [2,7,11,15], target = 9
## Output: [0,1]


class Solution:
    def twoSums(self, l:list, t:int) -> list:
        for i in range(len(l)):
            for j in range(i+1, len(l)):
                sum = l[i] + l[j]
                if sum == t:
                    return [i,j]

obj = Solution()
res = obj.twoSums([2,7,11,15],9)
print(res)