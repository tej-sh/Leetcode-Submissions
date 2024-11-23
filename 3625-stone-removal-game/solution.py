class Solution:
    def canAliceWin(self, n: int) -> bool:
        ans = False
        if 9<n<56:
            role = 0
            for i in range(10,0,-1):
                # print(n)
                n-=i
                # print(i)
                
                # print(n/)
                if n == 0:
                    
                    if role == 0:
                        ans = True
                    break
                elif n<0:
                    if role == 1:
                        ans = True
                    break
                    
                if role ==0:
                    role =1
                else:
                    role = 0
        return ans
                
                
