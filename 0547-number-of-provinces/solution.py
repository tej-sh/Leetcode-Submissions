class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        from collections import deque

        def bfs(adj,u):
            q = deque()
            visited[u] = True
            q.append(u)
            
            while q:
                r = q.popleft()
                for v in adj[r]:
                    if not visited[v]:
                        q.append(v)
                        visited[v] = True

            

        def dfs(adj,u):
            visited[u] = True

            for v in adj[u]:
                if not visited[v]:
                    dfs(adj,v)

        m = len(isConnected)
        adj = [[] for _ in range(m)]
        for i in range(m):
            for j in range(m):
                if i == j:
                    continue
                if isConnected[i][j] == 1:
                    adj[i].append(j)
        print(adj)
        visited = [False]*m
        res = 0
        for i in range(m):
            if not visited[i]:
                bfs(adj,i)
                res+=1
        return res
