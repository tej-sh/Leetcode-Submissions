class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        if len(s)%k != 0:
            return False
        l = len(s)//int(k)
        p1 = [s[i:i+l]for i in range(0,len(s),l) ]
        t1 = [t[j:j+l] for j in range(0,len(t),l)]
        return sorted(p1)==sorted(t1)
