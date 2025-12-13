class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        ans = []
        e,g,p,r = [],[],[],[]
        valid_business_line = {"electronics", "grocery", "pharmacy", "restaurant"}
        for i in range(len(code)):
            if (code[i] == '_' or code[i].replace('_','').isalnum()) and (businessLine[i] in valid_business_line) and isActive[i]:
                if businessLine[i] == 'electronics':e.append(code[i])
                elif businessLine[i] == 'grocery':g.append(code[i])
                elif businessLine[i] == 'pharmacy':p.append(code[i])
                elif businessLine[i] == 'restaurant':r.append(code[i])
        return sorted(e)+sorted(g)+sorted(p)+sorted(r)
        
        
