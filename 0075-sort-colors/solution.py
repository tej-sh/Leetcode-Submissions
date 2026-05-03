class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n =len(nums)
        for i in range(n):
            p1,p2 = 0,1
            while p2 <len(nums)-i:
                if nums[p1] > nums[p2]:
                    nums[p1],nums[p2] = nums[p2],nums[p1]
                p1+=1
                p2+=1

        
