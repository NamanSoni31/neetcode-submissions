class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = set()
        m = {}
        if len(nums) == 0:
            return 0
        for i in range(len(nums)):
            d.add(nums[i])

        for i in range(len(nums)):
            if nums[i] - 1 in d: 
                continue
            m[nums[i]] = 1
            val = nums[i]
            while val + 1 in d: 
                m[nums[i]] += 1
                val += 1

        return max(m.values())