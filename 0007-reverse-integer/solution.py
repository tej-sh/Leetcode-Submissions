class Solution:
    def reverse(self, x: int) -> int:
        flag = False
        if x<0:
            flag = True

        x = str(x)

        rev = x[::-1]
        s = len(x)
        if flag:
            rev = int(rev[:s-1:])
            if rev > 2**31 -1:
                return 0
            return 0-rev
        else:
            if int(rev) > 2**31 -1:
                return 0
            return int(rev)
            
