class Solution:
    def passwordStrength(self, password: str) -> int:
        res = 0
        s = "!@#$"
        password = set(password)
        for i in password:
            if "a"<= i <= "z":
                res +=1
            elif "A"<= i <= "Z":
                res+=2
            elif '0' <= i <= '9':
                res += 3
            elif i in s:
                res+=5
        return res
            
            
