class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=len)
        n = len(words)
        dp = [[-1]*(n+1) for _ in range(n)]

        def checkPred(word1,word2,m,n):
            
            p1 =0
            p2 =0

            while p1 <m and p2<n:
                if word1[p1] == word2[p2]:
                    p2+=1
                p1+=1
            if p2 >=n:
                return True
            return False


        def solve(idx,prev,length):
            
            if idx >= length:
                return 0

            if prev != -1 and dp[idx][prev] !=-1:
                return dp[idx][prev]

         
            take = 0
            if prev == -1:
                take = 1+solve(idx+1,idx,length)
            else:
                m = len(words[idx])
                n = len(words[prev])
            
                if m-n ==1 :
                    if checkPred(words[idx],words[prev],m,n):
                     take = 1+solve(idx+1,idx,length)
            skip = solve(idx+1,prev,length)

            if prev!=-1:
                dp[idx][prev] = max(take,skip)
            
            return max(skip,take)

        if n == 0:
            return 0
        if n==1:
            return 1
        
        return solve(0,-1,n)
            
            

