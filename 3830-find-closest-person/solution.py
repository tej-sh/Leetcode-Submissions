class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        mnX = abs(x-z)
        mnY = abs(y-z)
        if mnX == mnY:
            return 0
        elif mnX < mnY:
            return 1
        else:
            return 2


