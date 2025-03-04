class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        
        p1 = 0
        p2 = m-1
        while p1<n and p2 >=0:
            if target > matrix[p1][p2]:
                p1+=1
            elif target < matrix[p1][p2]:
                p2-=1
            else:
                return True
        return False

