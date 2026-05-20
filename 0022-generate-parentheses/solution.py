class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def solve(o,c,s):

            if o> n or c > n:
                return 
            if o < c:
                return 
            if o==n and c == n:
                res.append(s)
                return 
            
            
            open = solve(o+1,c,s+"(")
            close = solve(o,c+1,s+")")

            return 
        solve(0,0,"")
        return res






                    # (
        
#             (,(                 ()
    
#         (((     (()          ()(   ())-> X

# X ((((  ((()   (()( (())  ()((  ()()  

#    X ((()( ((())
