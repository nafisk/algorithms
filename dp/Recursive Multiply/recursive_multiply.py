'''
Recursive Multiply: Write a recursive function to multiply two positive integers without using the * operator.
You can use addition, subtraction, and bit shifting, but you should minimize the number of those operations.

#166 Think about multiplying 8 by 9 as counting the number of cells in a matrix with width 8 and height 9.
#203 If you wanted to count the cells in an 8x9 matrix, you could count the cells in a 4x9 matrix and then double it.
#227 Think about how you might handle this for odd numbers
#234 If there's duplicated work across different recursive calls, can you cache it?
#246 If you're doing 9*7 (both odd numbers), then you could do4*7 and 5*7.
#280 Alternatively, if you're doing 9 * 7, you could do 4*7, double that, and then add 7.

'''

def recursive_multiply(a, b):
    return a*b
    
# counting b iteratively
def recursive_multiply_count(a, b):
    res = 0
    for _ in range(a):
        res += b
    return res

# counting b recursively
def recursive_multiply_simple(a, b):
    if a == 0:
        return 0
    elif a == 1:
        return b
    else:
        return b + recursive_multiply_count(a-1, b)
    
# halving a and doubling b recursively
def recursive_multiply_half(a, b):
    print(a, b)
    if a == 0:
        return 0
    elif a == 1:
        return b
    else:
        half_a = a >> 1
        half_prod = recursive_multiply_half(half_a, b)
        if a % 2 == 0:
            return half_prod + half_prod
        else:
            return half_prod + half_prod + b

# memo'ed version
def recursive_multiply_memo(a, b, memo=None):
    if memo is None:
        memo = {}
    
    # base cases
    if a == 0:
        return 0
    if a == 1:
        return b
    if b == 1:
        return a
    
    # make a the smaller number
    if a > b:
        a, b = b, a
    
    # return memo'd result if available
    if (a, b) in memo:
        return memo[(a, b)]

    # process memo if not
    half_a = a >> 1
    half_prod = recursive_multiply_memo(half_a, b, memo)
    if a % 2 == 0:
        memo[(a, b)] = half_prod + half_prod
    else:
        memo[(a, b)] = half_prod + half_prod + b
    
    # return processed memo    
    return memo[(a, b)]


a, b = 2, 3
res = recursive_multiply(a, b)
print('recursive_multiply: ', res)

res = recursive_multiply_count(a, b)
print('recursive_multiply_count: ', res)

res = recursive_multiply_simple(a, b)
print('recursive_multiply_simple: ', res)

res = recursive_multiply_half(a, b)
print('recursive_multiply_half: ', res)

res = recursive_multiply_memo(a, b)
print('recursive_multiply_gpt: ', res)