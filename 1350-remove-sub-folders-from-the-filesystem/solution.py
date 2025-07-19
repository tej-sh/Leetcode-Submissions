class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        prev = folder[0]
        ans = []
        ans.append(folder[0])
        for i in range(1,len(folder)):
            l = len(prev)
            # print(f"check{i}")
            if len(folder[i]) > l and prev == folder[i][0:l] and folder[i][l] == '/':
                continue
            ans.append(folder[i])
            prev = folder[i]
        return ans
        
