class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        ans = []
        p1,p2 =0,n
        while p1<n and p2<2*n:
            ans.append(nums[p1])
            ans.append(nums[p2])
            p1+=1
            p2+=1
        return ans
