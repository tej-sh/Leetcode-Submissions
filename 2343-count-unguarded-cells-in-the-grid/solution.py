class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        def up(i,j):
            i-=1
            while i>=0:
                if mat[i][j] != 2 and mat[i][j]!=3 :
                    mat[i][j] = 1
                else:
                    break
                i-=1
            return
        def down(i,j):
            i+=1
            while i<m:
                if mat[i][j] != 2 and mat[i][j]!=3 :
                    mat[i][j] = 1
                else:
                    break
                i+=1
            return

        def left(i,j):
            j-=1
            while j>=0:
                if mat[i][j] != 2 and mat[i][j]!=3 :
                    mat[i][j] = 1
                else:
                    break
                j-=1
            return
        def right(i,j):
            j+=1
            while j<n:
                if mat[i][j] != 2 and mat[i][j]!=3 :
                    mat[i][j] = 1
                else:
                    break
                j+=1
            return

        mat = [[-1 for _ in range(n)] for _ in range(m)]

        for i,j in walls:
            mat[i][j] = 2

        for i,j in guards:
            mat[i][j] = 3

        for i,j in guards:
            left(i,j)
            up(i,j)
            down(i,j)
            right(i,j)
        
        c = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == -1:
                    c+=1
        return c
