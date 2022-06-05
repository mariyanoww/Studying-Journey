nums = str(input())
nums = list(map(int, nums.split()))
for a in range(0, len(nums)):
    nums[a] = -nums[a]
print(nums)
