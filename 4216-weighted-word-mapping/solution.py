class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        #97 122
        res = ""
        
        for word in words:
            x = 0
            for i in word:
                x+=weights[ord(i)-ord("a")]
            # print(x)
            # print(x%26)
            # print(122 - (x%26))
            x = x % 26
            res += chr(ord("z") - x)

        return res
