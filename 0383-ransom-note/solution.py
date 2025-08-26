class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        e = {}
        for i in ransomNote:
            d[i] = d.get(i,0)+1
        
        for i in magazine:
            e[i] = e.get(i,0)+1
        
        for i in d:
            if i in e:
                if e[i] < d[i]:
                    return False
            else:
                return False
        return True
