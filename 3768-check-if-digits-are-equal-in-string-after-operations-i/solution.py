class Solution:
    def hasSameDigits(self, s: str) -> bool:
        # flag = True
        s1 = ""
        # if len(s1) == 2:
        #     return s1[0] == s1[1]
        while True:
            prev = 0
            for i in range(1,len(s)):
                s1 += str((int(s[prev])+ int(s[i]))%10)
                prev = i
            # print(len(s1))
            if len(s1) == 2:
                break
            else:
                s = s1
                s1 = ""
        if s1[0] == s1[1]:
            return True
        return False

