class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = set()
        maxCons = 0
        for i in nums:
            d.add(i)

        for i in d:
            if i - 1 in d: 
                continue
            length = 1
            val = i
            while val + 1 in d: 
                length += 1
                val += 1
            if length > maxCons: 
                maxCons = length

        return maxCons