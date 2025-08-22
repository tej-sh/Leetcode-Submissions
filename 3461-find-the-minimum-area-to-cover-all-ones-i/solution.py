class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        l = -1
        r = -1
        start = -1
        end = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if l == -1 or l > j:
                        l = j
                    if r == -1 or r < j:
                        r = j
                    if start == -1:
                        start = i
                    end = i
        if l == -1 or r == -1:
            return 0
        
        end+=1
        r+=1

        return((end - start)*(r-l))
        
