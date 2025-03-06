class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        n = len(nums)
        p2 = 0
        while p2<n:
            if nums[p2] != val:
                nums[index] = nums[p2]
                index+=1
            p2+=1
        return index
