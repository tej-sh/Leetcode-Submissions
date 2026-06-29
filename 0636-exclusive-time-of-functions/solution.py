class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0]*n
        stack = []
        pos = 0
        for log in logs:
            id,mode,ts = log.split(":")
            id = int(id)
            ts = int(ts)
            
            if mode == "start":
                if stack:
                    res[stack[-1]] += ts-pos
                pos = ts
                stack.append(id)
            else:
               res[stack.pop()]+= ts-pos+1
               pos = ts+1

        return res

