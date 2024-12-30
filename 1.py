"""
nums = [2, 11, 15, 7]
target= 9
nums.sort()
resultado =[]
for i in range(0,len(nums)):
    objetivo = target - nums[i]
    if objetivo in nums and objetivo != nums[i]:
        resultado = [objetivo, nums[i]]
print(resultado)
"""

"""
nums = [2, 11, 15, 7]
print(list(enumerate(nums)))
"""
indexes = {}
nums = [3,3]
target = 6
for i, n in enumerate(nums):
    indexes[n] = i
print(indexes[3])
#print(len(indexes))
for i, n in enumerate(nums):
    objetivo = target - n
    if objetivo in nums and indexes[objetivo] != i:
        print(i, indexes[objetivo])


"""
seen = {}  
for i, num in enumerate(nums):
    complement = target - num  
    if complement in seen:
        return [seen[complement], i]  
    seen[num] = i
        
return []
"""