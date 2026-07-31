class Solution:
    def minimumPushes(self, word: str) -> int:
        from collections import defaultdict
        n = len(word)
        d = defaultdict(int)
        for i in word:
            d[i]+=1
        
        sorted_items = sorted(d.items(), key=lambda item: item[1], reverse=True)
        cost = defaultdict(int)
        x = 0
        curcost = 1
        for key,value in sorted_items:
            cost[key] = curcost
            x+=1
            if x >= 8:
                x=0
                curcost+=1
            
        res = 0
        for key in d:
            res += d[key]*cost[key]
        return res
