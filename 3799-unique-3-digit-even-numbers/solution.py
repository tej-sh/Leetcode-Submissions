class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        countarr = [0]*10
        for i in digits:
            countarr[i]+=1

        def check(d,countarr):
            for i in d.keys():
                if d[i] > countarr[i]:
                    return False
            return True

        ans  = 0      
        for k in range(100,1000):
            d = {}
            if k%2 !=0:
                continue
            for i in str(k):
                jk = int(i)
                
                if jk in d:
                    d[jk] +=1
                else:
                    d[jk] = 1
            if check(d,countarr):
                ans+=1
                # print(k)
        return ans
                    
                    
