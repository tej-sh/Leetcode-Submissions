class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        ini = 0

        for i in range(0,len(s),k):
            p = s[i:i+k]
            if(len(p)<k):
                p += fill*(k-len(p))
            ans.append(p)
        return ans
