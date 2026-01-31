class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        tar = ord(target)
        n = len(letters)
        m = 500
        ans = ""
        for i in range(n):
            if tar < ord(letters[i]) <= m:
                m = ord(letters[i])
                ans =  letters[i]
        return ans if ans != "" else letters[0]



