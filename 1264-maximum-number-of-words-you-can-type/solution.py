class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        c = 0
        s = text.split(" ")
        for i in s:
            for j in brokenLetters:
                if j in i:
                    break
            else:
                c+=1
        return c
