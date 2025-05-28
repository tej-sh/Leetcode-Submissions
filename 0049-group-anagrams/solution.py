class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in range(len(strs)):
            # print(strs[i])
            x = "".join(sorted(strs[i]))
            # print(x)
            if x in d:
                d[x].append(i)
            else:
                d[x]=[i]
        
        ans = []
        for i in d:
            med = []
            for j in d[i]:
                med.append(strs[j])
            ans.append(med)
        return ans
