class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
         
        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            x_parent = find(x)
            y_parent = find(y)
            if x_parent == y_parent:
                return
            if rank[x_parent] < rank[y_parent]:
                parent[x_parent] = y_parent
            elif rank[y_parent] < rank[x_parent]:
                parent[y_parent] = x_parent
            else:
                parent[x_parent] = y_parent
                rank[y_parent]+=1

        n = len(isConnected)
        rank = [0]*n
        parent = [i for i in range(n)]

        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j] ==1:
                    union(i,j)
        return sum(1 for i in range(n) if find(i) == i)
        
