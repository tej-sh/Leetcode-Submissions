class Solution:
    def maxDifference(self, s: str) -> int:
        #countarray
        arr = [0]*26
        n = len(arr)
        for i in s:
            x = ord(i) -97
            # print(x)
            arr[x] +=1
        arr.sort(reverse=True)
        odd = []
        even = []
        for i in arr:
            if i == 0:
                break
            if i %2 == 0:
                even.append(i)
            else:
                odd.append(i)
            
        return (max(odd) - min(even))

        
        #dictt
        # freq = {}
        # for i in s:
        #     if i in freq:
        #         freq[i] +=1
        #     else:
        #         freq[i] =1
        # print(freq)

        
        #dictionary
        #hashmap
