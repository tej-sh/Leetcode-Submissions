class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        n = len(cost)
        cost.sort(reverse = True)
        res = 0
        c = 0
        for i in range(n):
            if c!=2:
                res += cost[i]
                c += 1
            else:
                c = 0
        return res

