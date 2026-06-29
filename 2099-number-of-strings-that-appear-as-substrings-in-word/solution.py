class Solution:
    from collections import defaultdict

    def numOfStrings(self, patterns: List[str], word: str) -> int:
        d = defaultdict(str)
        res = 0
        for i in patterns:
            if i in word:
                res+=1
        return res
            
