class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = temperatures
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                idx =stack.pop()
                res[idx] = i - idx
            stack.append(i)
        while stack:
            res[stack.pop()] = 0
        return res
            
