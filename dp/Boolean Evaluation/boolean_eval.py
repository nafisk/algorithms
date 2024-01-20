'''
Boolean Evaluation: 
Given a boolean expression consisting of the symbols 0 (false), 1 (true), & (AND), I (OR), and A (XOR), 
and a desired boolean result value result, implement a function to count the number of ways of parenthesizing the expression 
such that it evaluates to result.

EXAMPLE
countEval("lA0l0ll", false) -> 2 countEval("0&0&0&1"ll0", true) -> 10

Hints:

#148 Can we just try all possibilities?What would this look like?
#168 We can think about each possibility as each place where we can put parentheses. This means around each operator. 
        such that the expression is split at the operator. What is the base case?
#197 The base case is when we have a single value, 1 or 0
#305 If your code looks really lengthy, with a lot of if's (for each possible operator, u target" boolean result and left/right side), 
        think about the relationship between the different parts. Try to simplify your code. It should not need a ton of complicated 
        if-state- ments. For example, consider expressions of the form <LEFT>OR<RIGHT> versus <LEFT>AND<RIGHT>. Both may need to know 
        the number of ways that the <LEFT> evaluates to true. See what code you can reuse
#327 Look at your recursion. Do you have repeated calls anywhere? Can you memoize it?
'''