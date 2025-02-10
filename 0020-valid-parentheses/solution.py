class Solution:
    def isValid(self, s: str) -> bool:
        d = {')':'(', '}':'{',']':'['}
        st = []
        for i in s:
            if i in ["(","{",'[']:
                st.append(i)
            else:
                if st:
                    if d[i] == st[-1]:
                        st.pop()
                    else:
                        print("here")
                        return False
                else:
                    return False
        return len(st)==0
