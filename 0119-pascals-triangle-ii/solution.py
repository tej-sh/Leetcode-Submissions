class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        res = [[1]*i for i in range(1,rowIndex+2)]
        for i in range(2,rowIndex+1):
            for j in range(1,i):
                res[i][j] = res[i-1][j]+res[i-1][j-1]
        return res[rowIndex]
