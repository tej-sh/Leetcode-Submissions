class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        x = bin(n)[2::]
        z = 0
        o = 0
        for i in x:
            if i == "0":
                z+=1
            else:
                o+=1
        if o == 1 and z%2 == 0 :
            return True
        return False


