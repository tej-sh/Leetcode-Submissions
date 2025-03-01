class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        c = 0
        j = 0
        for i in range(len(nums)):
            if nums[i] %2 ==0:
                c +=1
            else:
                j+=1

        l1 = [0]*c + [1]*j
        return l1
