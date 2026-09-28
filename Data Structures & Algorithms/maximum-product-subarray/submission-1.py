class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, curMin, curMax = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            maxVal = curMax * nums[i]
            minVal = curMin * nums[i]
            curMax = max(minVal, maxVal, nums[i])
            curMin = min(minVal, maxVal, nums[i])
            if max(curMin, curMax, nums[i]) > res: 
                res = max(curMin, curMax, nums[i])            
        return res