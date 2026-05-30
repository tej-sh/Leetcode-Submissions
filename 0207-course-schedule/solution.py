class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def cycle(u):
            visited[u] = True
            inRecursion[u] = True

            for v in adj[u]:
                if (not visited[v] and cycle(v)) or (visited[v] and inRecursion[v]):
                    return True
            inRecursion[u] = False
            return False



        adj = [[]for _ in range(numCourses)]
        visited = [False]*numCourses
        inRecursion = [False]*numCourses
        for u,v in prerequisites:
            adj[u].append(v)
        
        for u in range(numCourses):
            if not visited[u] and cycle(u):
                return False
        return True
        
     
        
        
        
        

