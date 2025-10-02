class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l = s.split(" ")
        if len(l) != len(pattern):
            return False
        d={}
        seen = set()
        for i in range(len(pattern)):
            if pattern[i] in d:
                if d[pattern[i]] != l[i]:
                    return False
            else:
                if l[i] in seen:
                    return False
                d[pattern[i]] = l[i]
                seen.add(l[i])
        return True
