class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # adj = [ [] for _ in range(n)]
        
        # for i in range(len(nums)-1):
        #     p1 = i+1
        #     while p1 < n:
        #         if abs(nums[p1] - nums[i]) <= maxDiff:
        #             adj[i].add(p1)
        #             adj[p1].add(i)
        #         p1+=1 
        res =[]
        parent = [i for i in range(n)]
        rank = [ 0 for _ in range(n)]

        def find(i):
            if i == parent[i]:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        
        def union(x,y):
            x_p = parent[x]
            y_p = parent[y]
            if x_p == y_p:
                return 
            if rank[x_p] > rank[y_p]:
                parent[y_p] = x_p
            elif rank[x_p] < rank[y_p]:
                parent[x_p] = y_p
            else:
                parent[x_p] = y_p
                rank[y_p] +=1

        # for i in range(len(nums)-1):
        #     p1 = i+1
        #     while p1 < n:
        #         if abs(nums[p1] - nums[i]) <= maxDiff:
        #             union(p1,i)
        #         else:
        #             break
        #         p1+=1 
        for i in range(n - 1):
            if nums[i+1] - nums[i] <= maxDiff:
                union(i, i+1)
        #print(parent)
        for query in queries:
            if parent[query[0]] == parent[query[1]]:
                res.append(True)
            else:
                res.append(False)
        return res

