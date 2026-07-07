class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = 0
        st = ""
        
        for i in str(n):
            if i != "0":
                s+=int(i)
                st+=i
        
        return int(st)*s if st!="" else 0
