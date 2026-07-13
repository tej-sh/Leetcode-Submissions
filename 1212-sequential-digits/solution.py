class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        window = "123456789"
        limit = [len(str(low)),len(str(high))]
        room = abs(limit[0]-limit[1])
        p1 = 0
        p2 = limit[0]
        while p2<=9:
            string = int(window[p1:p2])
            if string>=low and string<=high:
                res.append(string)
            p1+=1
            p2+=1
            for i in range(room):
                if p2+i <=9:
                    more = int(window[p1-1:p2+i])
                    if more>=low and more<=high:
                        res.append(more)
        # print(res)
        return sorted(res)
