class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        prev = words[0]
        for i in range(1,len(words)):
            if list(sorted(prev)) == list(sorted(words[i])):
                words[i] = "-1"  
            else:
                prev = words[i]
        s = []
        for i in words:
            if i != "-1":
                s.append(i)
        return s
