'''
MagicIndex:
A magic index in an array A[0..n-1] is defined to be an index such that A[i] = i. 
Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.

A = [-2, 0, 2, 4, 6, 8, 10]
      0, 1, 2, 3, 4, 5,  6
    
FOLLOW UP
What if the values are not distinct?
A = [-2, 0, 2, 4, 6, 5, 8, 10]
      0, 1, 2, 3, 4, 5, 6,  7
'''

# binary search solution
def magic_index(arr):
    
    if arr[0] == 0:
        return 0
    
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > mid:
            high = mid - 1
        elif arr[mid] < mid:
            low = mid + 1
        else:
            return mid
    
    return -1
    
# tests cases
val = magic_index([-2, 0, 2, 4, 6, 8, 10])
arr = [[-10, -5, 0, 3, 7, 9, 12, 13], # 3
       [0, 1, 2, 3, 4, 5], # any val
       [0, 1, 2, 3, 4, 5, 6, 7], # any val
       [-1, 0, 1, 2, 3, 4, 5, 7], # 7
       [-10, -5, -3, 0, 2, 5, 6, 10]] # 5

for a in arr:
    val = magic_index(a)
    print(val)








# binary search with duplicates
def find_magic_index_with_duplicates(arr, low, high):
    if low > high:
        return None

    mid = (low + high) // 2
    mid_value = arr[mid]

    if mid_value == mid:
        return mid

    # Search left and right, considering duplicates
    left_index = find_magic_index_with_duplicates(arr, low, min(mid - 1, mid_value))
    if left_index is not None:
        return left_index

    right_index = find_magic_index_with_duplicates(arr, max(mid + 1, mid_value), high)
    return right_index

# Usage
arr = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]
magic_index = find_magic_index_with_duplicates(arr, 0, len(arr) - 1)
print(magic_index)

    
