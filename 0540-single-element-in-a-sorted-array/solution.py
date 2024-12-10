class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if mid %2 ==0:
                if mid+1 ==len(nums):
                    return nums[mid]
                elif nums[mid+1] == nums[mid]:
                    low = mid+1
                else:
                    high = mid-1
            else:
                if mid+1 == len(nums):
                    return nums[mid]
                elif nums[mid+1]!= nums[mid]:
                    low = mid+1
                else:
                    high = mid-1
        return nums[low]

