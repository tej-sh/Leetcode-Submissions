class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pc = []
        left = []
        right = []
        for i in nums:
            if i == pivot:
                pc.append(i)
            elif i < pivot:
                left.append(i)
            else:
                right.append(i)
        return left+pc+right
            
