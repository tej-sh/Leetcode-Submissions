class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        c = 0
        for i in s:
            if i == "(":
                stack.append(i)
            else:
                if len(stack)!=0:
                    stack.pop()
                else:
                    c+=1
        while len(stack)!=0:
            c+=1
            stack.pop()
        return c
