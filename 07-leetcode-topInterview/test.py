nums=[10,20,7]
k=4


for i in range(k):
    nums.append(max(nums)//2)
    nums.remove(max(nums))
print(sum(nums))