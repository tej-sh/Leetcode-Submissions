class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        p1 = 0
        p2 = n-1
        
        while p1 <= p2:
            if s[p1] != " " and s[p2] != " " and s[p1].lower()!= s[p2].lower() and s[p1].isalnum() and s[p2].isalnum():
                return False
            if s[p1] == " " or not s[p1].isalnum():
                p1+=1
            elif s[p2] == " " or not s[p2].isalnum():
                p2-=1
            elif s[p1].lower() == s[p2].lower():
                p1+=1
                p2-=1
            
        return True
