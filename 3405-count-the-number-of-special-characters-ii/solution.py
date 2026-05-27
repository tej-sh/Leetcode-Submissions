class Solution:
    def numberOfSpecialChars(self, word: str) -> int:

        uc = {}
        lc = {}
        c = 0
        for i in range(len(word)):
            if word[i].isupper() and word[i] not in uc :
                uc[word[i]] = i
            elif word[i].islower():
                lc[word[i]] = i
        
        for i in lc:
            if i.upper() in uc and lc[i]< uc[i.upper()]:
                c+=1
        return c
                
        # lc = set()
        # uc = set()
        # c =0
        # for i in word:
        #     if i.islower():
        #         lc.add(i)
        #     else:
        #         uc.add(i)
        #         if i.lower() in lc:
        #             c+=1
        # return c

        # d = {}
        # c = 0
        # for i in word:
        #     if i.islower() and i not in d:
        #         d[i] = True
        #     elif i.isupper() and i.lower() in d and d[i.lower()]:
        #         d[i.lower()] = False
        #         c+=1

            
        # return c
