import random

nums = []

isComplete = False

while not isComplete:
    ranNum = random.randint(1,100)
    if len(nums) == 99:
        break
    if ranNum in nums:
        continue
    else:
        nums.append(ranNum)
nums.sort()
print(nums)