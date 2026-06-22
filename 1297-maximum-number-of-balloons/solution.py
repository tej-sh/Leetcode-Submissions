class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d ={
            "b":0,"a":0,"l":0,"o":0,"n":0
        }
        two = "lo"
        ans = float(inf)
        for i in text:
            if i in d:
                d[i] +=1
        
        for i in d:
            if i in two:
                ans = min(d[i]//2,ans)
            else:
                ans =min(d[i],ans)
        return ans if ans != float("inf") else 0
