class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        a,b = 0,0
        f = False
        c = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    a,b = i,j
                    f = True
                    break
            if f:
                break
        
        i,j = a,b
        i-=1
        while i>=0:
            if board[i][j] == 'B':
                break
            elif board[i][j] == 'p':
                c+=1
                break
            i-=1
        i,j = a,b
        i+=1
        while i<8:
            if board[i][j] == 'B':
                break
            elif board[i][j] == 'p':
                c+=1
                break
            i+=1
        i,j = a,b
        j-=1
        while j>=0:
            if board[i][j] == 'B':
                break
            elif board[i][j] == 'p':
                c+=1
                break
            j-=1
        i,j = a,b
        j+=1
        while j<8:
            if board[i][j] == 'B':
                break
            elif board[i][j] == 'p':
                c+=1
                break
            j+=1
        return c
        
                
