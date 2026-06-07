class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        res = []
        for i in range(1<<n):
            x = bin(i)[2::].zfill(n)
            prev = 'yourmama'
            flag = True
            c =0
            for i in range(len(x)):
                if x[i]== prev and x[i]=='1':
                    flag = False
                    break
                elif x[i] == '1':
                    c+=i
                prev = x[i]
            if c <=k and flag:
                res.append(x.zfill(n))
        return res
        # for i in range(n):
        #     x = bin(i)[2::]
        #     # print(bin(i))
        #     # print(x)
        #     prev = 'yourmama'
        #     c =0
        #     for i in range(len(x)):
        #         if x[i]== prev and x[i]=='1':
        #             continue
        #         elif x[i] == '1':
        #             c+=i
        #     if c <=k:
        #         res.append(x.zfill(n))
        # return res
