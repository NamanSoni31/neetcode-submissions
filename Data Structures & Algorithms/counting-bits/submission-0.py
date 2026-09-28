class Solution:
    def countBits(self, n: int) -> List[int]:
        res= [0]
        for i in range(1, n+1): 
            ones = 0
            mask = 1
            while mask <= i:
                if mask & i: 
                    ones += 1
                mask <<= 1
            res.append(ones)

        return res