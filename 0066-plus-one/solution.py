class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s1 = ""
        for i in digits:
            s1 += str(i)
        
        a = int(s1)+1
        result = []
        for i in str(a):
            result.append(int(i))
        return result
