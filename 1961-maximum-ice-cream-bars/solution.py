class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        cs =[0]*(max(costs)+1)
        count = 0
        for i in costs:
            cs[i]+=1
        print(cs)
        for i in range(len(cs)):
            if cs[i]!=0:
                if i > coins:
                    break
                else:
                    while cs[i] >0 and i <= coins:
                        count+=1
                        cs[i]-=1
                        coins -= i
        return count
    
