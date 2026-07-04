class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n+1)]
        visited = [False]*(n+1)
        for road in roads:
            adj[road[0]].append([road[1],road[2]])
            adj[road[1]].append([road[0],road[2]])
        res = float("inf")
        
        
        def solve(u):
            nonlocal res
            visited[u] = True
            for v,cost in adj[u]:
                res = min(res,cost)
                if not visited[v]:
                    solve(v)
        solve(1)
        return res
