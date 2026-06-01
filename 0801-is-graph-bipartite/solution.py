class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        from collections import deque
        def bfs(u,curColor):
            q = deque()
            color[u] = curColor
            q.append(u)

            while q:
                x = q.popleft()
                for v in graph[x]:
                    if color[v] == color[x]:
                        return False
                    elif color[v] == -1:
                        q.append(v)
                        color[v] = 1 - color[x]

            return True


        n = len(graph)
        color = [-1]*n
        
        for u in range(n):
            if color[u] == -1 and not bfs(u,1):
                return False

        return True
