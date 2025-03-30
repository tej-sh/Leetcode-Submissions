class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        n = len(s)
        ans = []
        p1 = 0
        p2 = 0

        while p1 < n:
            p2 = p1
            for i in range(p1,n):
                if s[i] in s[p1:p2+1]:
                    p2 = max(p2,s.rfind(s[i]))
            ans.append(p2-p1+1)
            p1 = p2 +1
        return ans
