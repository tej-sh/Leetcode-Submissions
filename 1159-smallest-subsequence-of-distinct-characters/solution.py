class Solution:
    def smallestSubsequence(self, s: str) -> str:

        alpha = [0]*(26)
        visited = [False]*(26)
        res = []
        for i in range(len(s)):
            alpha[ord(s[i])-97] = i
        
        for i in range(len(s)):
            if visited[ord(s[i])-97]:
                continue
            if len(res) == 0:
                res.append(s[i])
                visited[ord(s[i])-97] = True
                
            
            else:         
                while True:       
                    if res and res[-1] > s[i] and alpha[ord(res[-1])-97] > i and not visited[ord(s[i])-97]:
                        visited[ord(res[-1])-97] = False
                        res.pop()
                    else:

                        res.append(s[i])
                        visited[ord(s[i])-97] = True
                        break


        return "".join(res)
