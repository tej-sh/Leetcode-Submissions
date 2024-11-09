class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        print(n)
        i = n
        while(n!=0):
            j = str(i)
            product = 1
            print(f"j:{j}")
            for z in j:
                print(f"z{z}")
                product *= int(z)
            if product%t ==0:
                return i
            i+=1
