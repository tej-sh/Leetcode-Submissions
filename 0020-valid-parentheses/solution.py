class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        L = ['(','{','[']
        R = [')','}',']']
        ans = []
        for i in range(len(s)):
            if s[i] in L:
                ans.append(s[i])
            elif s[i] in R:
                ind = R.index(s[i])
                if len(ans)==0 or L[ind] != ans[-1]:
                    return False
                else:
                    ans.pop()
        if len(ans)==0:
            return True
        else:
            return False
            



