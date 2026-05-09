class Solution:
    def minFlips(self, s: str) -> int:
        if len(s) <= 2:
            return 0
        zCount = 0
        oCount = 0
        for i in s:
            if i == "0":
                zCount +=1
            else:
                oCount +=1
        #case-1 ig
        if oCount <= 1 or (oCount == 2 and s[0] == s[-1] and s[0] == "1"):
            return 0
        #case-2 
        if zCount == len(s) or oCount == len(s):
            return 0

        if s[0] == "1"and s[-1] == "1" :
            if oCount-2 < zCount:
                return oCount-2
        
        if zCount < oCount:
            return zCount
        else:
            return oCount -1 
        
