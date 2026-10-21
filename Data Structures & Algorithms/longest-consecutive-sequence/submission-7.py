class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = set()
        m = {}
        if len(nums) == 0:
            return 0
        for i in nums:
            d.add(i)

        for i in nums:
            if i - 1 in d: 
                continue
            m[i] = 1
            val = i
            while val + 1 in d: 
                m[i] += 1
                val += 1

        return max(m.values())