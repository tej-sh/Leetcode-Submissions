class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        mx = float('-inf')

        length = len(nums)
        prefix_sum = [0] * (length+1)

        for i in range(length):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
        
        for i in range(k):
            current_max = 0      
            for j in range(i, length-k+1, k):
                s = prefix_sum[j+k] - prefix_sum[j]
                current_max = max(s, current_max+s)
                mx = max(mx, current_max)

        return mx
