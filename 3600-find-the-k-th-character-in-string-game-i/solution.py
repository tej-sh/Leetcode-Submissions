class Solution:
    def kthCharacter(self, k: int) -> str:
        s = 'a'
        while k >= len(s):
            temp = ""
            for i in s:
                temp+= chr(ord(i)+1)
            s += temp
        return s[k-1]
        
