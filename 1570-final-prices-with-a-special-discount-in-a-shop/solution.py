class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []
        n = len(prices)
        for i in range(n-1):
            flag = True
            for j in range(i+1,n):
                if prices[i] >= prices[j]:
                    res.append(prices[i]-prices[j])
                    flag = False
                    break
            if flag:
                res.append(prices[i])
            
        res.append(prices[-1])
        return res

            
