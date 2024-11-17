class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        
        def result(i,direction):
            arr = nums[0::]
            # print(arr)
            cur = i
            reverse = 0
            if direction == 1:
                reverse = -1
            else:
                reverse = 1

            
            while 0<= cur <len(arr):
                if arr[cur] == 0:
                    cur += direction
                elif arr[cur]>0:
                    arr[cur]-=1
                    reverse,direction =direction,reverse
                    cur+=direction
            # print(arr.count(0))
            # print(arr)
            if arr.count(0) == len(arr):
                return True
            else:
                return False
            

        c = 0
        for i in range(len(nums)):
            if nums[i]==0:
                if result(i,1):
                    c+=1
                if result(i,-1):
                    c+=1
        return c
        
