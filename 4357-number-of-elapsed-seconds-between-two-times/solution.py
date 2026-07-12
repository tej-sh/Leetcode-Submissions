class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:

        x = startTime.split(":")
        y = endTime.split(":")

        start = int(x[0])*(60*60) + int(x[1])*60 + int(x[2])
        end = int(y[0])*(60*60) + int(y[1])*60 + int(y[2])
        
        return abs(start-end)
            
        
        return 0
