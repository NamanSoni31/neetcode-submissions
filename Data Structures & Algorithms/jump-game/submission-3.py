class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0
        for i in range(len(nums)):
            if i > maxReach: 
                return False
            reach = i + nums[i]
            if reach > maxReach: 
                maxReach = reach
            if maxReach >= len(nums)-1:
                return True
            
        return False