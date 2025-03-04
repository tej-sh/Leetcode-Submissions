class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 0:
            return 0
        if n==1:
            return 1
        p1 = 0
        p2 = 0
        c = 1
        while p1<n and p2<n:
            if nums[p2] != nums[p1]:
                p1+=1
                c+=1
                nums[p1] = nums[p2]
            else:
                
                p2+=1
 
        return c
