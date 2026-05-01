class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        total = 1
        if n ==0:
            return 0
        while n>1:
            temp = b
            b = a+b
            a = temp
            n-=1
        return b

# 0 1 1 2 3 5
