class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        maxLen = 0
        
        l = 0
        maxFreq = 0
        
        for r in range(len(s)):
            char = s[r]
            
            # update map with new char and increase maxFreq if approp
            count[char] += 1
            maxFreq = max(maxFreq, count[char])
            
            while (r - l + 1) - maxFreq > k and l < len(s):
                # remove beginning char and decrease window size
                count[s[l]] -= 1
                l += 1

            maxLen = max(maxLen, r - l + 1)
            
        return maxLen
