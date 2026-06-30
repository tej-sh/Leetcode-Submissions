class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        d = {"a":-1,"b":-1,"c":-1}
        res = 0
        for i in range(n):
            if s[i] in d:
                d[s[i]] = i
            if -1 not in d.values():
                res+= min(d.values())+1
        return res
