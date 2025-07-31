class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        target = "".join(sorted("balloon"))
        s = "".join(sorted(text))
        t = {}
        for i in target:
            if i in t:
                t[i] += 1
            else:
                t[i] = 1
        
        d = {}
        for i in s:
            if i in d and i in t:
                d[i] += 1
            else:
                if i in t:
                    d[i] = 1

        pos =""
        # print(d)
        # print(t)
        for i in t:
            if i in d:
                if pos == "":
                    pos = int(d[i]/t[i])
                else:
                    pos = min(pos,int(d[i]/t[i]))
            else:
                pos = 0
                return 0
        return pos
        
            


