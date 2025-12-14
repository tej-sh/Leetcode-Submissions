class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        flag = False
        j = 0
        for i in range(1,n+1):
            res.append('Push')
            if target[j] != i:
                res.append('Pop')
            if target[j] == i:
                if j == (len(target)-1):
                    return res
                j+=1
            
            # if flag:
            #     return res
