class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        hd = hour%12*30 + minutes*0.5
        md = minutes*6

        return min(abs(hd-md),360-abs(hd-md))

