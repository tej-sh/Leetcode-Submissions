class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
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
            elif rank[xp] > rank[yp]:
                parent[yp] = xp
            else:
                parent[yp] = xp
                rank[xp] +=1
        
            
        if len(connections) < n-1:
            return -1
        count = 0
        rank = [0]*n
        parent = [i for i in range(n)]
        # adj = [[] for _ in range(n)]
        k = set()
        c = 0
        components =n
        for connection in connections :
            u,v = connection
            k.add(u)
            k.add(v)
            if u<v:
                if find(u) != find(v):
                    components-=1
                    union(u,v)
        return components-1


        

        
