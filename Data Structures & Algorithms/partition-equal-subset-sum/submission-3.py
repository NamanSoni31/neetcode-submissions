class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        dp = {
            0: True
        }
        for i in nums:
            total += i
        
        if total % 2 == 0: 
            mid = total // 2
            for i in range(len(nums)):
                old_sums = list(dp.keys())
                for j in old_sums:
                    dp[j + nums[i]] = True
            if mid in dp and dp[mid] == True:
                return True
        return False