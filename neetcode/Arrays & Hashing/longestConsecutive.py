
def longestConsecutive(self, nums: List[int]) -> int:
    
    if not nums:
        return 0
    
    numSet = set(nums)     
    longest = 0
    
    for n in nums:
        
        if (n - 1) not in numSet:
            l = 0 # length
            while (n + l) in numSet:
                l += 1
            longest = max(longest, l)        
            
    
    return longest