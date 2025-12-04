class Solution:
    def countCollisions(self, directions: str) -> int:
        from collections import deque
        stack = deque()
        count = 0
        for i in directions:
            if not stack:
                stack.append(i)
            else:
                if stack[-1] == "L":
                    stack.append(i)
                elif stack[-1] == "R":
                    if i == "L" or i == "S":
                        if i == "L":
                            count+=2
                            stack.pop()
                        while stack and (stack[-1] == "R"):
                            count+=1
                            stack.pop()
                        stack.append("S")
                    else:
                        stack.append("R")
                else:
                    if i == "L":
                        count+=1
                    else:
                        stack.append(i)
        return count

