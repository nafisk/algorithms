'''
    💡 Top Down Approach
'''
# fib without memo
def fib(i):
    if i <= 0: return 0
    if i == 1: return 1
    return fib(i - 1) + fib(i - 2)


# fibonacci with memo
def fibMemo(val):
    memo = {0: 0, 1: 1}
    
    def helper(i):
        if i not in memo:
            memo[i] = helper(i - 1) + helper(i - 2)
        return memo[i]
    
    return helper(100)



'''
    💡 Bottom Up Approach
'''

# with array
def fibBotUp(val):
    if val <= 2: return 1
    
    arr = [0] * val
    arr[1] = 1
    
    for i in range(2, val):
        arr[i] = arr[i - 1] + arr[i - 2]
    return arr[-1] + arr[-2]


# without array
def fibBotUp_(val):
    if val <= 0: return 0
    a = 0
    b = 1
    
    for i in range(2, val):
        c = a + b 
        a = b
        b = c
    return a + b

if __name__ == '__main__':
    # print(fib(500))
    # print(fibMemo(500))
    # print(fibBotUp(16))
    # print(fibBotUp_(16))