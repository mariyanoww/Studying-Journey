def smallest(num):
    index = min(nums)
    return index


nums = []
for x in range(3):
    number = int(input())
    nums.append(number)
print(smallest(nums))

