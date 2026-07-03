class Solution:
    def findMaxPathScore(
        self, edges: List[List[int]], online: List[bool], k: int
    ) -> int:

        #dk
        n = len(online)

        graph = [[] for _ in range(n)]
        indegree = [0] * n

        for u, v, w in edges:
            graph[u].append((v, w))
            indegree[v] += 1

        from collections import deque

        q = deque()

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        topo = []

        while q:
            u = q.popleft()
            topo.append(u)

            for v, _ in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        def check(limit):
            INF = 10 ** 30

            dp = [INF] * n
            dp[0] = 0

            for u in topo:

                if dp[u] == INF:
                    continue

                if u != 0 and u != n - 1 and not online[u]:
                    continue

                for v, w in graph[u]:

                    if w < limit:
                        continue

                    if v != n - 1 and not online[v]:
                        continue

                    if dp[u] + w < dp[v]:
                        dp[v] = dp[u] + w

            return dp[-1] <= k

        left = 0
        right = 10 ** 9
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans





        # n = len(online)
        # adj = [[] for _ in range(n)]
        # for edge in edges:
        #     if online[edge[0]] and online[edge[1]]:
        #         adj[edge[0]].append([edge[1], edge[2]])

        
        # res = -1

        # def score(i,k):
        #     if online[i] == False or k<0:
        #         return -1
        #     mx = -1
        #     if i == n-1:
        #         return float("inf")
        #     for edge in adj[i]:
        #         adj_score = score(edge[0],k-edge[1])
        #         if adj_score != -1:
        #             curscore = min(edge[1] ,adj_score)
        #             mx = max(curscore,mx)

        #     return mx

        # return score(0,k)

