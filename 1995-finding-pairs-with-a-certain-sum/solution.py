class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq = {}
        for i in nums2:
            if i in self.freq:
                self.freq[i] +=1
            else:
                self.freq[i] = 1
        
    def add(self, index: int, val: int) -> None:
        old = self.nums2[index]
        new = old + val

        if new in self.freq:
            self.freq[new] +=1
        else:
            self.freq[new] = 1
        
        if self.freq[old]>1:
            self.freq[old] -=1
        else:
            del self.freq[old]
        
        self.nums2[index] = new

    def count(self, tot: int) -> int:
        c = 0
        for i in range(len(self.nums1)):
            target = tot-self.nums1[i]
            if target in self.freq:
                c+=self.freq[target]
                
            
        # for i in range(len(self.nums1)):
        #     target = tot - self.nums1[i] 
        #     for j in range(len(self.nums2)):
        #         if self.nums2[j] == target:
        #             c+=1
        #             # print("imhere")
        return c
    


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
