class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        word = set(word)
        # print(word)
        c = 0
        for i in word:
            if 'a' <= i <= 'z':
                if chr(ord(i)-32) in word:
                    c+=1
            
        return c
