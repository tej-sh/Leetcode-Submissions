class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        d = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        for i in s:
            if i in d.values() :
                stack.append(i)
            
            else:
                if not stack:
                    return False
                x = stack.pop()
                if x != d[i]:
                    return False
        if stack:
            return False
        return True
