    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        s1Map, s2Map = defaultdict(int), defaultdict(int)
        s1Map = dict(Counter(s1))
        
        l, r = 0, 0
        while r < len(s2):
            # add to map
            s2Map[s2[r]] += 1
        
            # window size should be len(s1)
            if r - l + 1 == len(s1):
                # found permutations with equal maps
                if s1Map == s2Map: 
                    return True
        
                # oversized window
                s2Map[s2[l]] -= 1
                if s2Map[s2[l]] == 0:
                    del s2Map[s2[l]]
                l += 1
            
            r += 1
            
        return False
