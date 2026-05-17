class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(goal)
        if n!= len(s):
            return False
        rcount = len(s)
        while rcount>0:
            goal = goal[n-1] + goal[0:n-1:]
            if goal == s:
                return True
            rcount-=1
        return False
