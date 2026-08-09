class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        @cache
        def solve(alice,i,M):
            # base
            if i>=n:
                return 0

            stones = 0
            result = -1 if alice ==1 else float("inf")
            for j in range(1,2*M+1):
                if i+j-1 >= n:
                    break
                stones += piles[i+j-1]
                if alice == 1:
                    result = max(result,stones+solve(0,i+j,max(M,j)))
                else:
                    result = min(result,solve(1,i+j,max(M,j)))
            return result


        n = len(piles)
        return solve(1,0,1)
