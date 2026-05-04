class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                print(i,j,matrix[i][j],matrix[j][i])
                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]
        
        for i in range(n):
            matrix[i] = matrix[i][::-1]
        
    

        # 00  01  02  03

        # 10  11  12  13

        # 20  21  22  23

        # 30  31  32  33
