class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        s = str(n)
        a = int(str(len(s)+1)*(len(s)+1))
        for i in range(n+1,a):
            s = str(i)
            d = {}
            for j in s:
                if j in d:
                    d[j]+=1
                else:
                    d[j]=1
            for k in s:
                if d[k] == int(k):
                    continue
                else:
                    break
            else:
                return i
        return a

