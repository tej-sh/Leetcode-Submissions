class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d = {}
        c = 0
        for i in dominoes:
            x = tuple(sorted(i))
            if x in d:
                c+=d[x]
                d[x]+=1
            else:
                d[x] = 1
        return c
