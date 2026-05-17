class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        n = len(boxGrid)
        m = len(boxGrid[0])
        rotatedBox = [["."]*n for _ in range(m)]
        print(rotatedBox)

        for i in range(n):
            l = 0
            for j in range(m):
                if boxGrid[i][j] == "#":
                    l+=1
                elif boxGrid[i][j] == "*":
                    rotatedBox[j][n-1-i] = "*"
                    if l>0:
                        k = j-1
                        while k >= 0 and l!=0:
                            rotatedBox[k][n-1-i]="#"
                            k-=1
                            l-=1
                
            
            if l > 0:
                k =m-1
                while k >= 0 and l!=0:
                    if rotatedBox[k][n-1-i] == ".":
                        rotatedBox[k][n-1-i]="#"
                        l-=1
                    k-=1
                    
        return rotatedBox
