class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = defaultdict(int)
        values = set(nums)
        if len(nums) == 0:
            return 0
        for num in values:
            if not num - 1 in values:
                value = num
                count[num] += 1
                while value + 1 in values:
                    value += 1
                    count[num] += 1
        return max(count.values())