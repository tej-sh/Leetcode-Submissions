class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s) 
        #brute force
        c = 0
        dp = [[-1]*1001 for _ in range(1001)]

        for i in range(n):
            for j in range(i+1,n+1):
                if dp[i][j] != -1:
                    c+=dp[i][j]
                else:
                    if s[i:j] == s[i:j][::-1]:
                        dp[i][j] = 1
                        c+=1
                    else:
                        dp[i][j] = 0

        return c
