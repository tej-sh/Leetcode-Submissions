class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        prev = -1
        flag = False
        for i in ((bin(n)[2::])):
            if prev == i and i=="1":
                if not flag:
                    flag = True
                else:
                    flag = False
                    return False
            prev = i
        # print(bin(30))
        if flag:
            return True
        return False
