class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(set(list((word))))
        # print(n)
        if n <= 8:
            return n
        s = n//8 
        rem = n%8
        first = 8*(s*(s+1)//2)
        sec = rem*(s+1)
        return first+ sec
