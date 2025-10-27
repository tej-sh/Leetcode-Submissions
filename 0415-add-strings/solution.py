class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        s = ""
        l1 = len(num1)-1
        l2 = len(num2)-1

        # print(ord(num1[0]) - ord('0'))

        while l1>=0 or l2>=0 or carry !=0:
            res = carry
            if l1>=0:
                res += ord(num1[l1]) - ord('0')
            if l2 >=0:
                res += ord(num2[l2]) - ord('0')
            l1-=1
            l2-=1
            s += chr(ord('0')+res%10) 
            carry = res//10
        s = s[::-1]
        return s
           
