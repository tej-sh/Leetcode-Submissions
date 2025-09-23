class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left,right+1):
            s = str(i)
            if '0' in s:
                continue
            # flag = True
            for j in s:
                if i%int(j) != 0:
                    break
            else:
                ans.append(i)
        return ans

