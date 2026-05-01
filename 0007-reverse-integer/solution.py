class Solution:
    def reverse(self, x: int) -> int:
        digits = str(x)
        if digits[0] == '-':
            digits = digits[1::]
            if int(digits[::-1]) > 2**31:
                return 0
            else:
                return 0 - int(digits[::-1])
        else:
            if int(digits[::-1]) > 2**31-1:
                return 0
            else:
                return int(digits[::-1])

   
