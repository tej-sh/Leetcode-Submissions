class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        s = 0
        started =False
        for i in range(len(nums)):
            if nums[i] == 1:
                if started:
                    if s < k:
                        return False
                    s = 0
                started = True
            else:
                if started:
                    s+=1
        return True
                

