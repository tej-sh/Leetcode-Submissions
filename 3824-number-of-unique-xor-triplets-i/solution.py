class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n<3:
            return n
        l = len(bin(n)[2:])
        # print(l)
        return 2**l
        

        # print(bin(1))
        # print(bin(2))
        # print(bin(3))
        # print(bin(4))
        # print(bin(5))
        # print(bin(6))
        # print(bin(20))
        # print(bin(7))
