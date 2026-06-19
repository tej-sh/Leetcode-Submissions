class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        mx = 0
        s = 0
        for i in gain:
            s += i
            mx = max(s,mx)
        return mx

