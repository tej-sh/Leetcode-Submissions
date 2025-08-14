class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = {}
        for path in paths:
            d[path[0]] = path[1]
    
        city = path[0]
        while city in d:
            city = d[city]
        return city
