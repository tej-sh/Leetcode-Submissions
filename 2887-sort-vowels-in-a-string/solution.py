class Solution:
    def sortVowels(self, s: str) -> str:
        d = {
            'A':0,
            'E':0,
            'I':0,
            'O':0,
            'U':0,
            'a':0,
            'e':0,
            'i':0,
            'o':0,
            'u':0,
        }
        for i in s:
            if i in d:
                d[i] += 1
        ans = ""
        for i in s:
            if i in d:
                for j in d:
                    if d[j] > 0:
                        ans+= j
                        d[j]-=1
                        break
            else:
                ans+=i
        return ans
