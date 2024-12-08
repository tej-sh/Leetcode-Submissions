class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result =[]
        n = len(nums)
        for i in range(n):
            if nums[i]>0:
                result.append(nums[(i+nums[i])%n])
            elif nums[i] == 0:
                result.append(nums[i])
            elif nums[i]<0:
                req = abs(nums[i])
                x = (i-req+n)%n
                result.append(nums[x])
        return result
