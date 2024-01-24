def productExceptSelf(self, nums: List[int]) -> List[int]:
    multRight = [1] * len(nums)
    multLeft = [1] * len(nums)
    
    # Create the multRight array
    for i in range(1, len(nums)):
        multRight[i] = multRight[i - 1] * nums[i - 1]
        
    # Create the multLeft array
    prevVal = 1
    for i in range(len(nums) - 1, -1, -1):
        multLeft[i] = prevVal
        prevVal *= nums[i]
    
    # Combine the two arrays to get the final result
    result = []
    for i in range(len(nums)):
        result.append(multRight[i] * multLeft[i])
    
    return result