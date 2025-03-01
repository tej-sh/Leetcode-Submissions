class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        check = strs[0]
        n = len(strs)
        
        for i in range(1,n):
            while not strs[i].startswith(check):
                check = check[:-1]
                if not check:
                    return ""
        return check





        # s = ""
        # for i in range(n):
        #     for j in range(len(check)):
        #         if j >= len(strs[i]):
        #             break
        #         else:
        #             if check[j] == strs[i][j]:
        #                 if len(s) == 0:
        #                     s+=check[j]
        #                 else:
        #                     if s[j] != check[j]:
        #                         s = s[:-1]
                                
        #                         return s
        #             else:
        #                 print("ho")
        #                 return s
