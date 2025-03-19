class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        c = 0
        for i in range(n):
            if nums[i] ==0:
                nums[i] = 1
                if i + 1 >= n:
                    return -1
                
                nums[i+1] ^=1

                if i +2 >= n:
                    return -1
                nums[i+2]^=1
                c+=1
        # print(nums)
        # print(sum(nums))
        # print(n)
        if sum(nums) == n:
            return c

        return -1

