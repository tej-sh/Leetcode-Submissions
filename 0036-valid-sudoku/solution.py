class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] != "." and board[i][j] not in seen:
                    seen.add(board[i][j])
                elif board[i][j]==".":
                    continue
                else:
                    return False

        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] != "." and board[j][i] not in seen:
                    seen.add(board[j][i])
                elif board[j][i]==".":
                    continue
                else:
                    return False

        for i in range(0,9,3):
            for j in range(0,9,3):
                seen = set()
                for k in range(3):
                    for l in range(3):
                        if board[i+k][j+l] in seen:
                            print(seen)
                            print(i,j,k,l)
                            return False
                        else:
                            if board[i+k][j+l] != ".":
                                seen.add(board[i+k][j+l])
        return True


