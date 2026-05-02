class Solution:
    def check(self, nums: List[int]) -> bool:
        flag = False
        prev = nums[0]
        for i in range(1,len(nums)):
            if nums[i] - prev < 0:
                if flag:
                    return False
                flag = True
            prev = nums[i]
            if flag and nums[-1] > nums[0]:
                return False

        return True 
