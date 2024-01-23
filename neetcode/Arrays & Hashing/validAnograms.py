import collections

def isAnagram(s, t):
    countS, countT = collections.defaultdict(int), collections.defaultdict(int)
    
    if len(s) != len(t): return False
    
    for i in range(len(s)):
        countS[s[i]] += 1
        countT[t[i]] += 1
        
    for key, val in countS.items():
        if countT[key] != val:
            return False
        
    return True
        