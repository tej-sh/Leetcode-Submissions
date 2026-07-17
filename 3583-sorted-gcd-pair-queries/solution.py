class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        exact = [0] * (mx + 1)

        for g in range(mx, 0, -1):
            cnt = 0
            for m in range(g, mx + 1, g):
                cnt += freq[m]

            pairs = cnt * (cnt - 1) // 2

            k = 2 * g
            while k <= mx:
                pairs -= exact[k]
                k += g

            exact[g] = pairs

        prefix = [0] * (mx + 1)
        for g in range(1, mx + 1):
            prefix[g] = prefix[g - 1] + exact[g]

        ans = []
        for q in queries:
            ans.append(bisect_right(prefix, q))
        return ans
            


        # dp = {}
        # n = len(nums)
       
        # arr = []
        
        # for i in range(n):
        #     for j in range(n):
        #         if j!=i:
        #             if (i,j) in dp or (j,i) in dp:
        #                 continue
        #             dp[(i,j)] = math.gcd(nums[i],nums[j])
        #             arr.append(dp[(i,j)])
        # arr.sort()
        # res = []
        # for i in queries:
        #     res.append(arr[i])
        # return res
