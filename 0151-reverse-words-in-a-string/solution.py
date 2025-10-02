class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        
        l = list(s.split(" "))
        print(l)
        ans = ""
        for i in range(len(l)-1,-1,-1):
            if l[i] == '':
                continue
            else:
                ans += l[i]
                if i != 0:
                    ans+= " "
        # print(ans)
        return ans       
