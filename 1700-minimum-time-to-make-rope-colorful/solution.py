class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev = 0
        c = 0
        for i in range(1,len(colors)):
            if colors[prev] == colors[i]:
                if neededTime[prev] < neededTime[i]:
                    c += neededTime[prev]
                    prev = i
                else:
                    c+=neededTime[i]
            else:
                prev = i
        return c

