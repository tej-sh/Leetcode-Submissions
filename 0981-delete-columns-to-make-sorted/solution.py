class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        c = 0
        for i in range(len(strs[0])):
            prev = 0
            for j in range(len(strs)):
                if prev <= ord(strs[j][i]):
                    prev = ord(strs[j][i])
                else:
                    c+=1
                    break
        return c
