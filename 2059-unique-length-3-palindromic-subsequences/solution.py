class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left ={}
        n = len(s)
        c = 0
        for i in range(n):
            if s[i] not in left:
                left[s[i]] = i
        used = set()
        for i in range(n-1,-1,-1):
            if s[i] in left and left[s[i]]!=i and s[i] not in used:
                if i - left[s[i]] >=2 :
                    c += len(set(s[left[s[i]]+1:i]))
                    used.add(s[i]) 
        return c
