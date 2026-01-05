class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        mn = float("inf")
        s = 0
        c = 0
        for i in range(n):
            for j in range(n):
                mn = min(mn,abs(matrix[i][j]))
                if matrix[i][j] < 0:
                    c+=1
                s += abs(matrix[i][j])
                
        if c%2 ==0:
            return s
        else:
            print(s)
            return s-abs(mn)*2
        

