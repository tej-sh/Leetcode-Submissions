class Solution:
    def romanToInt(self, s: str) -> int:
        value = 0
        dict1 = {"I":1, "V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        bI = ["V","X"]
        bX = ["L","C"]
        bC = ["D","M"]
        for i in range(len(s)-1):
            if s[i] == "I":
                if s[i+1] not in bI:
                    value += 1
                else:
                    value -= dict1["I"]
            elif s[i] == "X":
                if s[i+1] not in bX:
                    value+=dict1["X"]
                else:
                    value -= dict1["X"]
            elif s[i]=="C":
                if s[i+1] not in bC:
                    value+=dict1["C"]
                else:
                    value -=dict1["C"]
            else:
                value+=dict1[s[i]]
        value+= dict1[s[len(s)-1]]
        return value
