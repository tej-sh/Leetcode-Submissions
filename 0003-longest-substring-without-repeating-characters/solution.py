class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prev = 0
        sl =0
        d = {}
        m = 0
        i = 0
        n = len(s)
        while i<n:
            if s[i] in d and d[s[i]] >= prev:
                while prev <=d[s[i]]:
                    prev+=1
                    sl -=1
        
            d[s[i]] = i
            sl+=1
            m = max(m,sl)
            i+=1
        return m

