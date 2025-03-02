class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        a = s[0]
        m = 1  
        c = 0
        n = len(s)
        for i in range(n):
            #even
            p1 = i
            p2 = i+1
            while p1>=0 and p2<n:
                if s[p1]==s[p2]:
                    p1-=1
                    p2+=1
                else:
                    break
            c = p2-p1-1
            if m < c:
                a = s[p1+1:p2]
                m =c 
            
            
            #even
            p1 = i
            p2 = i
            while p1>=0 and p2<n:
                if s[p1]==s[p2]:
                    p1-=1
                    p2+=1
                else:
                    
                    break
            c = p2-p1-1
            if m < c:
                a = s[p1+1:p2]
                m = c

        return a
