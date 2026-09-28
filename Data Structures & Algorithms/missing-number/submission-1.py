class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        val = 0
        for i in range(len(nums) + 1):
            res = res ^ i
        for j in nums: 
            val = val ^ j
        
        return res ^ val