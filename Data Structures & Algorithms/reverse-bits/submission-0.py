class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        i = 0
        while i < 32: 
            mask = 1
            mask <<= i
            if mask & n: 
                new_mask = 1
                new_mask <<= 31 - i
                res += new_mask
            i += 1
        return res