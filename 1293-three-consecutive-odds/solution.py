class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        s = 0
        for i in arr:
            if i%2 != 0 :
                s += 1
                # print(i)
            else:
                if s >= 3:
                    return True
                s = 0
        if s >=3 :
            return True
        else:
            return False
            
