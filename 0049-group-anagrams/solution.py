class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            if "".join(sorted(list(i))) in d:
                d["".join(sorted(list(i)))].append(i)
            else:
                d["".join(sorted(list(i)))] = [i]
        res = []
        for i in d:
            res.append(d[i])
        return res
