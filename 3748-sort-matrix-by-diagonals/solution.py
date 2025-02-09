class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        for i in range(n):
            s = []
            for j in range(n-i):
                if j != j+i:
                    s.append(grid[j][j+i])
            s.sort()
            C=0
            for k in range(n-i):
                
                if k!=k+i and C<len(s):
                    grid[k][k+i] = s[C]
                    C += 1
        for i in range(n):
            s = []
            for j in range(n-i):
                s.append(grid[j+i][j])
            s.sort(reverse=True)
            C=0
            for k in range(n-i):
                grid[k+i][k] = s[C]
                C+=1
        
        return grid
