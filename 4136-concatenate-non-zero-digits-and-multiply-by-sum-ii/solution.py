class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        prefix = []
        sm = 0
        st = 0
        mod = 10**9+7
        l = 0
        for i in s:
            sm += int(i)
            if i!="0":
                st = (st*10+int(i))%mod
                l+=1
            prefix.append([sm%mod,st%mod,l%mod])
        # print(prefix)
        res = []
        for query in queries:
            x,y = query[0],query[1]
            if x == 0:
                prefix_sum = prefix[y][0]
                prefix_str = prefix[y][1]

                res.append((prefix_str*prefix_sum)%mod)
            else:
                prefix_sum = prefix[y][0] - prefix[x-1][0]
                prefix_str = (prefix[y][1] - prefix[x-1][1]*pow(10, prefix[y][2]-prefix[x-1][2], mod)) % mod                # print(prefix[y][1]%mod)
                # print(prefix[x-1][1],prefix[x-1][2])
                # print(prefix[x-1][1]*(10**(prefix[x-1][2])))
                # print("--------")
                res.append((prefix_str*prefix_sum)%mod)

        return res
