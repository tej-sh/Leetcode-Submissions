class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n =len(s)
        def rev(l,r):
            if l>=n//2:
                return 
            s[l],s[r] = s[r],s[l]
            return rev(l+1,r-1)
        rev(0,n-1)

