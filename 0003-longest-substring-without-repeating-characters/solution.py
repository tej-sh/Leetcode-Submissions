class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        d = {}
        l = 0
        res = 0
        for i in range(n):
            if s[i] in d and d[s[i]]>=l:
                l =  d[s[i]]+1
            d[s[i]] = i 
            res = max(res ,i - l +1)
            
        return res
