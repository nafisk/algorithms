def search(self, nums, target):
    l, r = 0, len(nums) - 1
    
    # l <= r because it needs to be equals to find the target in the array
    while l <= r:

        midIndex = l + (r - l) // 2

        if target < nums[midIndex]:
            r = midIndex - 1
        elif target > nums[midIndex]:
            l = midIndex + 1
        else:
            return midIndex      

    return -1