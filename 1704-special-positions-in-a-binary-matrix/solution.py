class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def check(i,j,m,n):
            for k in range(n):
                if k == j:
                    continue
                if mat[i][k] == 1:
                    return False
            for k in range(m):
                if k == i:
                    continue
                if mat[k][j] == 1:
                    return False
            return True

        m =len(mat)
        n = len(mat[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    if check(i,j,m,n):
                        ans+=1
        return ans
                
