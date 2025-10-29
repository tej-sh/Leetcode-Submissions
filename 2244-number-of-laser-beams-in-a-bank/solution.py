class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        c = 0 
        res = 0
        for i in bank:
            cur = i.count("1")
            if cur == 0:
                continue
            else:
                res += c*cur
                c = cur
        return res
