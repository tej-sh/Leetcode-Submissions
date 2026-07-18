class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        x_v = ""
        y_v = ""
        res = ""
        for i in s:
            if i == x:
                x_v+=i
            elif i == y:
                y_v+=i
            else:
                res+=i
        return res+y_v+x_v
        
