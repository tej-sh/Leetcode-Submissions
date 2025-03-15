class Spreadsheet:

    def __init__(self, rows: int):
        self.rows = rows
        self.gd = [[0]*26 for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        row = int(cell[1:]) - 1
        self.gd[row][ord(cell[0])- ord('A')] = value
        
    def resetCell(self, cell: str) -> None:
        row = int(cell[1:]) - 1
        self.gd[row][ord(cell[0]) - ord("A")] = 0

    def getValue(self, formula: str) -> int:
        x = list(formula[1:])
        a = ""
        b = ""
        got = 0
        for i in x:
            if i == "+":
                got = 1
                continue
            if got == 0 :
                a+=i
            else:
                b += i
        

        ans = 0
        if a[0].isalpha():
            row = int(a[1:]) - 1
            col = ord(a[0]) - ord('A')

            ans += self.gd[row][col]

        else:
            ans += int(a)

        if b[0].isalpha():
            row = int(b[1:]) -1 
            col = ord(b[0]) - ord('A')

            ans += self.gd[row][col]

        else:
            ans += int(b)
        
        return ans
# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
