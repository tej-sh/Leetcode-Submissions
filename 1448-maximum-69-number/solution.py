class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        ans = ""
        for i in range(len(s)):
            if s[i] == "9":
                ans+="9"
            else:
                ans+="9"
                if s[i+1::]:
                    ans+= s[i+1::]
                break
        return int(ans)
