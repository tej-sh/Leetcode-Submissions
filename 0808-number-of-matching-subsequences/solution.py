import bisect
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        c = 0
        az = [[] for _ in range(26)]

        for i in range(len(s)):
            az[ord(s[i])-97].append(i)
        


        for word in words:
            current = -1
            flag = True
            for j in range(len(word)):
                ele = ord(word[j])-97
                if len(az[ele]) == 0:
                    flag = False
                    break
                x = bisect_right(az[ele], current)
                if x == len(az[ele]):
                    flag = False
                    break
                current = az[ele][x]
            if flag:
                c+=1
        return c

            


