from collections import defaultdict

def containsDuplicate(nums):
    counts = defaultdict(int)

    for num in nums:
        counts[num] += 1
        if counts[num] > 1:
            return True

    return False

# Test cases
nums_1 = [1, 2, 3]
assert containsDuplicate(nums_1) is False
print('✅ Test 1')

nums_2 = [1, 2, 1]
assert containsDuplicate(nums_2) is True
print('✅ Test 2')

nums_3 = [1, 2, 3, 4]
assert containsDuplicate(nums_3) is False
print('✅ Test 3')