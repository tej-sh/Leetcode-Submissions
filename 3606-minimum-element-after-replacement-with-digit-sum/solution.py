class Solution:
    def minElement(self, nums: List[int]) -> int:
        mn = float("inf")
        for i in nums:
            x = 0
            for j in str(i):
                x+= int(j)
            mn = min(x,mn)
        return mn
