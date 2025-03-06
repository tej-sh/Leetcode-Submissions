class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        start = -1
        c = 0
        for i in range(n-1,-1,-1):
            if s[i] != " " and start == -1:
                start = s[i]
            if s[i]==" " and start != -1:
                break
            if start != -1:
                c+=1

        # print(start)
        # print(s[i])
        return c
