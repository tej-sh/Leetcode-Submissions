class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rank = [0]*(len(edges)+1)
        parent = [ _ for _ in range(len(edges)+1)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            xp = find(x)
            yp = find(y)

            if xp == yp:
                return
            
            if rank[xp] < rank[yp]:
                parent[xp] = yp
            elif rank[yp] < rank[xp]:
                parent[yp] = xp
            else:
                parent[xp] = yp
                rank[yp] += 1
        
        for edge in edges:
            x,y = edge
            if find(x) == find(y):
                return [x,y]
            union(x,y)
        return []

