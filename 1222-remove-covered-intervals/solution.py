class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        res = len(intervals)

        for i in range(len(intervals)):
            for j in range(len(intervals)):
                if i!= j and intervals[i][0] >= intervals[j][0] and intervals[i][1]<= intervals[j][1]:
                    res -=1
                    break
        return res
