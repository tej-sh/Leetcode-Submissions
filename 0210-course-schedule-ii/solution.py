class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import deque
        
        degree = [0]*numCourses
        adj = [[]for _ in range(numCourses)]

        for u,v in prerequisites:
            adj[u].append(v)
            degree[v] +=1

        q = deque()
        res = deque()

        for z in range(numCourses):
            if degree[z] == 0:
                q.append(z)
       
        while q:
            p = q.popleft()
            res.appendleft(p)

            for v in adj[p]:
                if degree[v] <= 0:
                    continue
                degree[v] -=1
                if degree[v] == 0:
                    q.append(v)
        
        return list(res) if len(res) == numCourses else []
 
