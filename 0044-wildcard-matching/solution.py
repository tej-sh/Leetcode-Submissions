class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p1 = 0
        p2 = 0
        star = -1
        temp = -1
        while p1 < len(s):
            if p2 < len(p) and (s[p1] == p[p2] or p[p2] == '?'):
                p1+=1
                p2+=1
            elif p2 < len(p) and p[p2] == '*':
                star = p2
                temp = p1
                p2+=1
            elif star !=-1:
                p2 = star + 1
                temp +=1
                p1 = temp 
            else:
                return False
        while p2<len(p) and p[p2] == '*':
            p2+=1
        return p2 == len(p)
