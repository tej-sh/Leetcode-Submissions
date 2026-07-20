class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        total = m*n
        onedih = []
        for i in range(n):
            for j in range(m):
                onedih.append(grid[i][j])
        
        k = k%total
        
        onedih =  onedih[-k:] + onedih[:total-k]
        idx = 0
        for i in range(n):
            for j in range(m):
                grid[i][j] = onedih[idx]
                idx+=1
        return grid
