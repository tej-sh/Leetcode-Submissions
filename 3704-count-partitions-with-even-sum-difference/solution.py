class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        c = 0
        n = len(nums)
        for i in range(1,n):
            x = nums[0:i]
            s1 = sum(x)
            y = nums[i:n]
            s2 = sum(y)
            # print(x,y)
            if (s1+s2)%2 == 0 :
                c+=1
        return c
