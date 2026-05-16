class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = -1
        d = {}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            if d[i]==1:
                for j in range(len(s)):
                    if s[j] == i:
                        return j
        return -1
