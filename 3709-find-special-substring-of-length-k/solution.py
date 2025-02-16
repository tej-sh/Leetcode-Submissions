class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        p1 = 0
        p2 = 0
        x = 0
        flag = False
        while p2<len(s):
            if s[p1] == s[p2]:
                x+=1
            else:
                x =1
                p1=p2
                
            if x == k:
                b = p1-1 <0 or s[p1-1]!=s[p1]
                a = p2+1 >=len(s) or s[p2+1]!=s[p2]
                if a and b:
                    return True
            
            p2+=1
        return False
                
