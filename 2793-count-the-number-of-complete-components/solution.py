class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # adj = [[] for _ in range(n)]
       
        # visited = [False]*n
        from collections import defaultdict
    

        parent = [i for i in range(n)]
        rank = [0]*n

        def find(i):
            if parent[i] == i:
                return parent[i]
            parent[i] = find(parent[i])
            return parent[i]
        
        def union(x,y):
            xp = find(x)
            yp = find(y)
            if xp == yp:
                return 
            if rank[xp] > rank[yp]:
                parent[yp] = xp
            elif rank[yp] > rank[xp]:
                parent[xp] = yp
            else:
                parent[xp] = yp
                rank[yp] += 1
        # res = [[] for _ in range(n)]
        temp = defaultdict(int)
        for u,v in edges:
            union(u,v)
        for u,v in edges:
            # if parent[u] == parent[v]:
            #     temp[find[u]] +=1
            temp[find(u)]+=1
                # res[find(u)].append(u)
                # res[find(u)].append(v)
            
        nodes = defaultdict(int)
        for i in range(n):
            nodes[find(i)] += 1
        res = 0
        for k,v in nodes.items():
            c = v*(v-1)//2
            if c == temp[k]:
                res +=1
        return res


        # d={"a":1,"b":2, "c":3}

        # for x,y in d.items():
        #     print(x,y)
        

