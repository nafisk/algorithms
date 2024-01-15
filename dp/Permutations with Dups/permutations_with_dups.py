'''
Permutations without Dups: 
    Write a method to compute all permutations of a string of unique characters.
'''

def permute(string):
    
    def helper(strLst):

        if len(strLst) == 1:
            return [tuple(strLst[:])]
        
        res = set()
        
        for _ in range(len(strLst)):
            n = strLst.pop(0)
            perms = helper(strLst)
            
            for perm in perms:
                perm = list(perm)
                perm.append(n)
                res.add(tuple(perm))
            
            # res.add(perms)
            strLst.append(n)
        
        return res
    
    print(helper(list(string)))
    return -1

arr1 = "aab"
res = permute(arr1)
print(res)
