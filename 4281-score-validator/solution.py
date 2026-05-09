class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        counter = 0
        score = 0

        d1 = {
            "0":0,
            "1":1,
            "2":2,
            "3":3,
            "4":4,
            "6":6
        }

        if counter >= 10:
            return [score,counter]
        
        
        for i in events:
           
            if i in d1:
                score+= d1[i]
            else:
                if i == "W":
                    counter+=1
                elif i=="WD":
                    score += 1
                elif i=="NB":
                    score += 1
            if counter >=10:
                return [score,counter]
        return [score,counter]
