class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        a = []
        
        a.append(startTime[0])
        
        for i in range(1, n):
            a.append(startTime[i] - endTime[i - 1])
        
        a.append(eventTime - endTime[n - 1])
        
        b = sum(a[:k + 1])
        result = b
        
        for i in range(k + 1, len(a)):
            b += a[i] - a[i - (k + 1)]
            result = max(result, b)
        return result
