class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        flag = False
        for i in range(len(nums)):
            if nums[i]==1:
                flag = True
            elif 0 >= nums[i] or nums[i] > len(nums):
                nums[i] = 1
        if not flag:
            return 1
        
        for i in range(len(nums)):
            idx = abs(nums[i]) -1
            if nums[idx] > 0:
                nums[idx] = 0 - nums[idx]
        
        for i in range(len(nums)):
            if nums[i] >0 :
                # print("i+1",nums)
                return i+1

        return len(nums)+1
