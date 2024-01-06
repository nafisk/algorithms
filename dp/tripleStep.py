
import time
"""

8.1 Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. 
Implement a method to count how many possible ways the child can run up the stairs.

[1, 2, 3]

i = 1

def count(array):

    numWays = 0
    def helper(i):
        nonlocal numWays
        if i == len(array):
            numWays += 1
            return

        if i > n:
            return

        for j in range(1, 4):
            helper(i+j)

    helper(0)
    return numWays
"""

# def tripleStep(arr):
#     numWays = 0


#     def helper(i, path):
#         nonlocal numWays
#         # If the current index is exactly at the last element of the array, increment numWays.
#         if i == len(arr) - 1:
#             numWays += 1
#             path.append(arr[i])
#             print(path)
#             return

#         # If the current index goes beyond the end of the array, return.
#         if i >= len(arr):
#             return

#         path.append(arr[i])
#         # Try hopping 1, 2, or 3 steps from the current position.
#         for j in range(1, 4):
#             helper(i + j, path)
#         path.remove(arr[i])

#     helper(0, [])
#     return numWays

# Example usage
# arr = [1, 2, 3]
# 1 -> 2 -> 3 = 1
# 1 -> 3

# 1 -> 2 = 1   2 -> 3
# 1 -> 3

# print(tripleStep(arr))



"""

n = 100

if n == 0:
    return 1
if n < 0:
    return 0

return n - 1 ++ n - 2 ++ n - 3

#152: Approach this from the top down. What is the very last hop the child made?
#178: If we knew the number of paths to each of the steps before step 100, could we compute the number of steps to 100?
#217: We can compute the number of steps to 100 by the number of steps to 99, 98, and 97. 
    This corresponds to the child hopping 1, 2, or 3 steps at the end. 
    Do we add those or multiplythem?That is: lsit f{100) = f{99) + f{98) + f{97) orf(100) = f{99) * f{98) * f(97)?
#237: We multiply the values when it's uwe do this then this:•we add them when it's "we do this or this:"
#262: What is the runtime of this method? Think carefully. Can you optimize it?
#359: Try memoization as a way to optimize an inefficient recursive program.

Base cases:
stay where you are

"""

def tripleStep(n):
    if n == 0:
        return 1
    if n < 0:
        return 0

    return tripleStep(n - 1) + tripleStep(n - 2) + tripleStep(n - 3)


def tripleStepMemo(steps):
    memo = {}
    
    def helper(n):
        if n in memo:
            return memo[n]

        if n == 0:
            return 1
        if n < 0:
            return 0

        memo[n] = tripleStep(n - 1) + tripleStep(n - 2) + tripleStep(n - 3)
        return memo[n]
    
    return helper(steps)


"""GPT ans
Top Down
Time Comp: O(n)
Space Comp: O(n)
"""
def tripleStepTopDown(n, memo=None):
    if memo is None:
        memo = {}
    if n == 0:
        return 1
    if n < 0:
        return 0
    if n not in memo:
        memo[n] = tripleStepTopDown(n - 1, memo) + tripleStepTopDown(n - 2, memo) + tripleStepTopDown(n - 3, memo)
    return memo[n]


"""
Bottom up

"""

n = 3
i = 2
ways = [1, 0, 1, 2] # 2

def tripleStepBottomUp(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    ways = [0] * (n + 1)
    ways[0] = 1  # Base case

    for i in range(1, n + 1):
        ways[i] += ways[i - 1] if i - 1 >= 0 else 0
        ways[i] += ways[i - 2] if i - 2 >= 0 else 0
        ways[i] += ways[i - 3] if i - 3 >= 0 else 0

    return ways[n]


n = 6
start = time.time()
print(tripleStepTopDown(n))
end = time.time()
print((end - start) * 1000000)

start = time.time()
print(tripleStepBottomUp(n))
end = time.time()
print((end - start) * 1000000)