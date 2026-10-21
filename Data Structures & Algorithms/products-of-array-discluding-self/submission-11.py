class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        prefix = 1
        suffix = 1

        for i in range(n):
            res[i] *= prefix
            res[n - i - 1] *= suffix

            prefix *= nums[i]
            suffix *= nums[n - i - 1]
        
        return res