class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        augumented = '1'+ s + '1'
        segmented = []
        seg = s[0]
        for i in range(1,n):
            if seg[-1] != s[i]:
                segmented.append(seg)
                seg = s[i]
            else:
                seg+=s[i]
        segmented.append(seg)
        totalones = s.count("1")
        res = totalones
        for i in range(1,len(segmented)-1):
            if segmented[i][0] == '1' and segmented[i-1][0]=='0' and segmented[i+1][0]=="0":
                remaining_ones = totalones-len(segmented[i])
                res = max(res,len(segmented[i])+len(segmented[i-1])+len(segmented[i+1])+remaining_ones)

        return res
        
       
            




