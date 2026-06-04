class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict
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
                rank[yp] +=1
        
        rank = [0]*n
        parent = [ i for i in range(n)]

        for edge in edges:
            x,y = edge
            union(x,y)
        d = defaultdict(int)
        for i in range(n):
            p = find(i)
            d[p] += 1
        rem = n
        res = 0
        for i in d:
            res += d[i]*(rem-d[i])
            rem -= d[i]
        return res
            
