class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        
        ans = []
        for i in range(len(nums)-k+1):
            d = {}
            if i+k-1 < len(nums):
                for j in range(i,i+k):
                    if nums[j] in d:
                        d[nums[j]] +=1
                    else:
                        d[nums[j]] = 1
                a = (sorted(d.items(),key =lambda item: (item[1] , item[0]), reverse = True))
                s = 0
                # print(nums[i:k])
                # print(d)
                # print(a)
                for j in range(min(x,len(a))):
                    s+=a[j][0]*a[j][1]
                    
                ans.append(s)
            else:
                break
        return ans
