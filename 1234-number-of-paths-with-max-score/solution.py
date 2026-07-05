class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        
        n = len(board)
        m = len(board[0])

        i,j = n-1,m-1
        #0,0 target
        # mx = 0
        # count = 0
        dp = {}
        def solve(i,j):
            if board[i][j] == "E":
                return [0,1]
            if board[i][j] == "X":
                return [0,0]
            if (i,j) in dp:
                return dp[(i,j)]

            upath,uscore,lscore,lpath,dscore,dpath =0,0,0,0,0,0

            if (i-1>=0 and j>=0 and board[i-1][j]!="X"):
                [score,path] = solve(i-1,j)
                uscore,upath = score,path
                if upath >0:
                    if board[i-1][j] != 'S' and board[i-1][j]!='E':
                        uscore += int(board[i-1][j])

            if (i>=0 and j-1>=0 and board[i][j-1]!="X"):
                [score,path] = solve(i,j-1)
                lscore,lpath = score,path
                if lpath >0:
                    if board[i][j-1] != 'S'and board[i][j-1]!='E':
                        lscore += int(board[i][j-1])
            
            if (i-1>=0 and j-1>=0 and board[i-1][j-1]!="X"):
                [score,path] = solve(i-1,j-1)
                dscore,dpath = score,path
                if dpath >0:
                    if board[i-1][j-1] != 'S'and board[i-1][j-1]!='E':
                        dscore += int(board[i-1][j-1])
            
            bestscore,bestpaths =0,0

            if uscore==lscore==dscore and uscore!=0:
                bestscore = uscore
                bestpaths = upath+lpath+dpath
            elif uscore == lscore and lscore !=dscore:
                bestscore = uscore
                bestpaths = upath+lpath
                if dscore>uscore:
                    bestscore = dscore
                    bestpaths = dpath
            elif uscore == dscore and lscore !=dscore:
                bestscore = uscore
                bestpaths = upath+dpath
                if lscore>uscore:
                    bestscore = lscore
                    bestpaths = lpath
            elif dscore == lscore and lscore !=uscore:
                bestscore = lscore
                bestpaths = dpath+lpath
                if dscore<uscore:
                    bestscore = uscore
                    bestpaths = upath
            else:
                bestscore = uscore
                bestpaths = upath
                if lscore > dscore and lscore>bestscore:
                    bestscore = lscore
                    bestpaths = lpath
                if dscore > bestscore and lscore<dscore:
                    bestscore = dscore
                    bestpaths = dpath
                if upath == 0 and bestpaths == 0:
                    if dpath > 0 and dscore == bestscore:
                        bestpaths = dpath
                    elif lpath > 0 and lscore == bestscore:
                        bestpaths = lpath
            dp[(i,j)] = [bestscore,bestpaths%((10**9)+7)]
            return [bestscore,bestpaths%((10**9)+7)]
        return solve(n-1,m-1)
        # def solve(i,j,cursum):
        #     nonlocal mx,count
        #     if i < 0 or j < 0:
        #         return 
            
        #     if i == 0 and j ==0:
        #         if mx < cursum:
        #             mx = cursum
        #             count = 1
        #         elif mx == cursum:
        #             count+=1
        #         return 


        #     if board[i][j] == "X":
        #         return
            
        #     if board[i][j] == "S":
        #         up = solve(i-1,j,cursum)
        #         left = solve(i,j-1,cursum)
        #         left_diag = solve(i-1,j-1,cursum)
        #     else:
        #         up = solve(i-1,j,cursum+int(board[i][j]))
        #         left = solve(i,j-1,cursum+int(board[i][j]))
        #         left_diag = solve(i-1,j-1,cursum+int(board[i][j]))
        #     return 

        # solve(n-1,m-1,0)
        # return [mx,count]

            


