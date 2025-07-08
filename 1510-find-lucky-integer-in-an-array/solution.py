class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d ={}
        arr.sort(reverse=True)
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i] =1
        
        for i in d:
            if i == d[i]:
                return i
        return -1
        # for key,value in d:
        #     if key == value:
        #         return key
        # return -1
