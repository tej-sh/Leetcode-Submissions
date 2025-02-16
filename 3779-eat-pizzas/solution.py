class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        ans = 0 
        n=len(pizzas)
        pizzas.sort(reverse = True)
        days = n//4
        odd = (days+1)//2
        even = days - odd
        def evenans():
            x = 0
            for i in range(even):
                
                x += pizzas[odd + 2*i+1]
            
            return x
        ans += evenans()
        ans += sum(pizzas[:odd])
        return ans
