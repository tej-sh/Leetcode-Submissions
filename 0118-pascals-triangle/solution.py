class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        res = [[1]*i for i in range(1,numRows+1)]
        for i in range(2,numRows):
            for j in range(1,i):
                res[i][j] = res[i-1][j]+res[i-1][j-1]
        return res
