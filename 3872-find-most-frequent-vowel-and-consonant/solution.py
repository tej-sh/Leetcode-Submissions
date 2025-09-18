class Solution:
    def maxFreqSum(self, s: str) -> int:
        d = {'a':0,'e':0,'i':0,'o':0,'u':0}
        l = {}
        mxv = 0
        mxc = 0
        for i in s:
            if i in d:
                d[i] +=1
            else:
                if i in l:
                    l[i] += 1
                else:
                    l[i] = 1
        
        for i in d:
            mxv = max(mxv,d[i])
        for i in l:
            mxc = max(mxc,l[i])
        return mxc + mxv
