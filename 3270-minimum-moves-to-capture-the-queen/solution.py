class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:

        # bishop first
        x,y = c,d
        while x>0 and y>0:
            if x==e and y==f:
                return 1
            if x == a and y == b:
                break
            x-=1
            y-=1

        x,y = c,d
        while x<9 and y<9:
            if x==e and y==f:
                return 1
            if x == a and y == b:
                break
            x+=1
            y+=1

        x,y = c,d
        while x>0 and y<9:
            if x==e and y==f:
                return 1
            if x == a and y == b:
                break
            x-=1
            y+=1

        x,y = c,d
        while x<9 and y>0:
            if x==e and y==f:
                return 1
            if x == a and y == b:
                break
            x+=1
            y-=1

        # rook next
        p,q = a,b
        while p>0:
            if p == e and q == f:
                return 1
            if p == c and q == d:
                break
            p-=1 

        p,q = a,b
        while p<9:
            if p == e and q == f:
                return 1
            if p == c and q == d:
                break
            p+=1 

        p,q = a,b
        while q<9:
            if p == e and q == f:
                return 1
            if p == c and q == d:
                break
            q+=1 

        p,q = a,b
        while q>0:
            if p == e and q == f:
                return 1
            if p == c and q == d:
                break
            q-=1 

        return 2

