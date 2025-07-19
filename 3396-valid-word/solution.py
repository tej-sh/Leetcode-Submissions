class Solution:
    def isValid(self, word: str) -> bool:
        vow = ['a','e','i','o','u','A','E','I','O','U']
        vc = False
        cc = False
        if len(word)>=3 :
            if word.isalnum():
                for i in word:
                    if i in vow:
                        vc = True
                    elif i.isalpha():
                        cc = True
                if vc and cc:
                    return True
        return False
                    
                
