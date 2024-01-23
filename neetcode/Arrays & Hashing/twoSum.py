def twoSum(nums, target):
    
    hashmap = {}
    
    for i in range(len(nums)):
        comp = target - nums[i]
        
        if comp in hashmap:
            compIndex = hashmap[comp]
            return [compIndex, i]
        else:
            hashmap[nums[i]] = i
    
    
    return []
