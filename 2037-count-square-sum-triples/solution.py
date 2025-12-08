l = []
for i in range(0,251):
    l.append(i**2)
class Solution:
    def countTriples(self, n: int) -> int:
        a = 0
        for i in range(n+1):
            for j in range(i+1,n+1):
                if l[j]+l[i] in l[j+1:n+1]:
                    a+=2
        # print(l)
        return a
