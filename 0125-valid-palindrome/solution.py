class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        s = s.lower()
        p1 = 0
        p2 = n-1
        while (p1<n and p2>=0):
            if not s[p1].isalnum():
                p1+=1
                continue
            elif not s[p2].isalnum():
                p2-=1
                continue
            if s[p1]!=s[p2]:
                return False
            p1 +=1
            p2 -=1
        return True
