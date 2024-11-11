class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            x = haystack.index(needle)
            return x
        except:
            return -1
