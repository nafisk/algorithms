"""
Coins: Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), 
and pennies (1 cent), write code to calculate the number of ways of representing n cents.

# Hints:
300: Try breaking it down into subproblems. If you were making change, what is the first choice you would make?
324: If you were making change, the first choice you might make is how many quarters you need to use.
343: Think about how infinite loops might occur.
380: Analyze your algorithm. Is there any repeated work? Can you optimize this?
394: Have you thought about security and reliability?
Try using memoization.
"""


# backtracking
import math

def coin_change_backtracking_top_down(n):
    coins = [1, 5, 10, 25]
    minCoins = math.inf

    def helper(val, numCoins):
        nonlocal minCoins

        if val < 0:
            return
        
        if val == 0:
            minCoins = min(minCoins, numCoins)
            return

        for coin in coins:
            helper(val - coin, numCoins + 1)

        return minCoins
    
    return helper(n, 0)


# backtracking with memo
import math

def coin_change_backtracking_top_down_memo(n):
    coins = [1, 5, 10, 25]
    memo = {0: 0}  # Base case: 0 coins are needed to make 0 value

    def helper(val):
        if val < 0:
            return math.inf

        if val in memo:
            return memo[val]

        # Initialize minimum for the current value as infinity
        min_coins = math.inf

        # Try each coin and store the minimum coins needed
        for coin in coins:
            result = helper(val - coin)
            min_coins = min(min_coins, result + 1)

        memo[val] = min_coins
        return memo[val]

    result = helper(n)
    return result if result != math.inf else -1



# Bottom - Up approach
def coin_change_bottom_up(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    print(dp)

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
                print(f'{i} - {coin} = {i - coin}')
                print(dp)
                print()
    return dp[amount] if dp[amount] != amount + 1 else -1


coins = [1, 5, 10, 25]
res = coin_change_bottom_up(coins, 27) # 5, 1, 1 = 3 coins
print(res)