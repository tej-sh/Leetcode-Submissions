class Solution:
    def intToRoman(self, num: int) -> str:
        # d= {"I":1,"V":5 ,"X":10,"L":50,"C":100,"D":	500,"M":1000}
        # uh = {4 :"IV", 9 :"IX", 40 :"XL", 90 :"XC", 400 :"CD",900 :"CM"}
        
        ans = ""

        while num!=0:
            if num >= 1000:
                ans += "M"
                num -= 1000
            elif num >= 500:
                if num >= 900:
                    ans+='CM'
                    num -= 900
                else:
                    ans+='D'
                    num -= 500
            elif num >= 100:
                if num >= 400:
                    ans += 'CD'
                    num -= 400
                else:
                    ans += 'C'
                    num-= 100
            elif num >=50:
                if num >=90:
                    num-=90
                    ans+="XC"
                else:
                    num-=50
                    ans+="L"
            elif num >=10:
                if num >=40:
                    ans+= "XL"
                    num-=40
                else:
                    ans+="X"
                    num-=10
            elif num >= 5:
                if num ==9:
                    ans+="IX"
                    num-= 9
                else:
                    num-=5
                    ans+="V"
            elif num <5:
                if num<4:
                    ans+="I"
                    num-= 1
                else:
                    ans+="IV"
                    num -= 4
        return (ans)


