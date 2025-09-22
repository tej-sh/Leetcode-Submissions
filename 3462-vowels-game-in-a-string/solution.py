class Solution:
    def doesAliceWin(self, s: str) -> bool:
        c = 0
        for i in s:
            if i in "aeiouAEIOU":
                return True
        return False
