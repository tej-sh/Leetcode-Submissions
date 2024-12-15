class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        maxvalue=0
        minindex = 0
        for i in range(len(events)):
            if i == 0 :
                time = events[i][1]
            else:
                time = events[i][1]-events[i-1][1]
            if maxvalue < time:
                maxvalue = time
                minindex = events[i][0]
            elif maxvalue == time:
                minindex = min(minindex,events[i][0])
        return minindex
            
