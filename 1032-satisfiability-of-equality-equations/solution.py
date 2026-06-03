class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        rank = [0]*26
        parent = [ i for i in range(26)]

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
                parent[xp] = yp
        
        queries = []
        for i in equations:
            if i[1] == "!":
                queries.append(i)
            else:
                x = ord(i[0]) - ord('a')
                y = ord(i[3]) - ord('a')
                union(x, y)

        
        for i in queries:
            x = ord(i[0]) - ord('a')
            y = ord(i[3]) - ord('a')

            if find(x) == find(y):
                return False
        return True
        

        # d = {}
        # for i in equations:
        #     if i[0] in d and i[3] in d:
        #         if i[1] == "=":
        #             if d[i[0]] not in d[i[3]] or d[i[3]] not in d[i[0]]:
        #                 return False
        #             d[i[0]].append(i[3])
        #             d[i[3]].append(i[0])
        #         else:
        #             if d[i[0]] in d[i[3]] and d[i[3]] in d[i[0]]:
        #                 return False
        #     elif i[0] in d:
        #         if i[1] == "!":
        #             d[i[3]] = [i[0]]
        #             d[i[0]].append(i[3])
        #         else:
        #             d[i[3]] = []
        #     elif i[3] in d:
        #         if i[1] == "!":
        #             d[i[0]] = [i[3]]
        #             d[i[3]].append(i[0])
        #         else:
        #             d[i[0]] = []
        #     else:
        #         if i[1] == "=":
        #             d[i[0]] = [i[3]]
        #             d[i[3]] = [i[0]]
        #         else:
        #             d[i[0]] = []
        #             d[i[3]] = []
        # return True
