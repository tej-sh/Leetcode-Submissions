class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][j] = -3892839284
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == -3892839284:
                    matrix[i][j] = 0
                    for k in range(m):
                        if matrix[k][j] != -3892839284:
                            matrix[k][j] = 0
                    for l in range(n):
                        if matrix[i][l] != -3892839284:
                            matrix[i][l] = 0

        
