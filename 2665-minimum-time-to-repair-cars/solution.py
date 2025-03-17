class Solution:

    #CHATTTTTTTTTTTTTTTTTTTTTTT


    def repairCars(self, ranks: List[int], cars: int) -> int:
        def check(time):
            s = 0
            for i in ranks:
                s += int(math.sqrt(time/i))
                if s >= cars:
                    return True
            return s>=cars
        
        lo = 0
        high = min(ranks)*cars*cars
        res = high
        while lo<=high:
            mid = (lo+high)//2
            if check(mid):
                res = mid
                high = mid -1
            else:
                lo = mid + 1
        return res
