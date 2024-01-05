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