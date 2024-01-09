"""
Write a method to return all subsets of a set. 
Hints: #273, #290, #338, #354, #373

#273 How can you build all subsets of {a, b, c} from the subsets of {a, b}?
#290 Anything that is a subset of {a, b} is also a subset of {a, b, c}. Which sets are subsets of {a, b, c} but not {a, b}?
#338 Subsets that contain c will be subsets {a, b, c} but not {a, b}. Can you build these subsets from the subsets of {a, b}?
#354 You can build the remaining subsets by adding c to all the subsets of{a, b}
#373 You can also do this by mapping each subset to a binary number. The ith bit could representauboolean"flag for whether an element is in the set

# Example:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

# Subsets with Duplicates
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Both solutions have a 
Time Complexity: O(2^n)
Space Complexity: O(2^n)
"""

# subsets without duplicates
def subsets(nums):
    res = []
    subset = []

    def dfs(i):
        if i == len(nums):
            res.append(subset[:])
            return

        # take val
        subset.append(nums[i])
        dfs(i + 1)

        # don't take val
        subset.pop()
        dfs(i + 1)

    dfs(0)
    return res


# subsets with duplicates
def subsetDups(nums):
    res = []
    subset = []
    nums.sort()

    def dfs(i):
        if i == len(nums):
            res.append(subset[:])
            return

        # take val
        subset.append(nums[i])
        dfs(i + 1)

        # don't take val
        subset.pop()
        
        # skip duplicates
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        dfs(i + 1)

    dfs(0)
    return res


arr1 = [1, 2, 2]
res = subsetDups(arr1)
print(res)