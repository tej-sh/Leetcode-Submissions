class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n >0:
            if n.bit_count()==1:
                return True
        return False
