class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        
        queue = []
        visited = [[False for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    queue.append([i,j])
                    visited[i][j] = True

        
        arr = [[0 for _ in range(m)] for _ in range(n)]
        while queue:
            i,j = queue.pop(0)
            if i-1 >= 0 and not visited[i-1][j]: #top
                queue.append([i-1,j])
                if arr[i-1][j] == 0:
                    arr[i-1][j] = arr[i][j]+1
                    visited[i-1][j] = True
            if j-1 >=0 and not visited[i][j-1]: #left
                queue.append([i,j-1])
                if arr[i][j-1]==0:
                    arr[i][j-1] = arr[i][j]+1
                    visited[i][j-1] = True 
            if i+1 <n and not visited[i+1][j]:
                queue.append([i+1,j])
                if arr[i+1][j]==0:
                    arr[i+1][j] = arr[i][j]+1
                    visited[i+1][j] = True
            if j+1 < m and not visited[i][j+1]:
                queue.append([i,j+1])
                if arr[i][j+1]==0:
                    arr[i][j+1] = arr[i][j]+1
                    visited[i][j+1] = True
        # for i in range(n):
        #     print(arr[i])

        def solve(i,j,mid):
            if arr[i][j]< mid:
                return False
            que =[[i,j]]
            visited = [[False for _ in range(m)] for _ in range(n)]
            visited[i][j] = True
            directions = ([-1,0],[0,-1],[1,0],[0,1]) #🥀

            while que:
               
                i,j = que.pop(0)
                if i == n-1 and j == m-1:
                        return True
                for direction in directions:
                    x = direction[0]+i
                    y = direction[1]+j
                     
                    if x < n and x >= 0 and y >= 0 and y<m and not visited[x][y]:
                        
                        if arr[x][y] >= mid:
                            visited[x][y] = True
                            que.append([x,y])
            return False
        #bfs
        #solve(0,0,0)
        low = 1
        high = max(m,n)
        res = 0
        while low <= high:
            mid = (low+high)//2
            if solve(0,0,mid):
                res = mid
                low = mid+1
            else:
                high = mid-1
            
        return res




        # def solve(i,j,sf):
        #     if i >= n and j >= m:
        #         return 0
        #     if i == n-1 and j == m-1:
        #         if grid[i][j]==1:
        #             return float("inf")
                
        #         for theif in theifs:
        #             md = abs(i-theif[0]) + abs(j-theif[1])
        #             cs = min(sf,md)
                

        #     if grid[i][j] == 1:
        #         return float("inf")
            
        #     down = solve(i+1,j,sf)
        #     right = solve(i-1,j,sf)
