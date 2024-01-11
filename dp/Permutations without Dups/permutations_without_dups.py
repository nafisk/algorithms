'''
Permutations without Dups: 
    Write a method to compute all permutations of a string of unique characters.

#150: Approach 1: Suppose you had all permutations of abc. How can you use that to get all permutations of abed?
#185: Approach 1: The permutations of abc represent all ways of ordering abc. Now, we want to create all orderings of abed. Take a specific ordering of abed, such as bdea. This bdea string represents an ordering of abc, too: Remove the d and you get bca. Given the string bea, can you create all the "related"orderings that included, too?
#200: Approach 1: Given a string such as bca, you can create all permutations of abed that have {a, b, c} in the order bca by inserting d into each possible location: dbca, bdca, bed a, bead. Given all permutations of abc, can you then create all permutations of abed?
#267: Approach 1:You can create all permutations of abed by computing all permutations of abc and then inserting d into each possible location within those.
#278: Approach2:If you had all permutations of two-characters ubstrings, could you generate all permutations ofthree-charactersubstrings?
#309: Approach 2: To generate a permutation of abed, you need to pick an initial character. It can be a, b, c, or d. You can then permute the remaining characters. How can you use this approach to generate all permutations of the full string?
#335: Approach 2: To generate all permutations of abed, pick each character (a, b, c, or d} as a starting character. Permute the remaining characters and prepend the starting character. How do you permute the remaining characters? With a recursive process that follows the same logic.
#356: Approach 2: You can implement this approach by having the recursive function pass back the list of the strings, and then you prepend the starting character to it. Or, you can push down a prefix to the recursive calls.
'''

def permute(string):
    
    def helper(strLst):

        if len(strLst) == 1:
            return [strLst[:]]
        
        res = []
        
        for _ in range(len(strLst)):
            n = strLst.pop(0)
            perms = helper(strLst)
            
            for perm in perms:
                perm.append(n)
            
            res.extend(perms)
            strLst.append(n)
        
        return res
    
    res = helper(list(string))    
    return [''.join(r) for r in res]

arr1 = "abc"
res = permute(arr1)
print(res)
