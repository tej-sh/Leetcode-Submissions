class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # s = sum(nums)
        s = 0
        p1 = 0
        while p1<len(nums):
            if nums[p1]%3 ==0:
                p1+=1
            else:
                if (nums[p1]-1)%3 == 0:
                    s+=1
                    p1+=1
                elif (nums[p1]+1)%3 == 0:
                    s+=1
                    p1+=1
                else:
                    s+=2
                    p1+=1
        return s

