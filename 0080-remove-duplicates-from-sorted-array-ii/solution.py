class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        if len(nums) == 0:
            return 0

        
        c = 1
        idx = 1
        for i in range(1,len(nums)):
            if nums [i]== nums[i-1]:
                c+=1
            else:
               
                c = 1
            if c <=2: 
                nums[idx] = nums[i]
                idx += 1
        return idx
