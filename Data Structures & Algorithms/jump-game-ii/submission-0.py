class Solution:
    def jump(self, nums: List[int]) -> int:
        maxReach = 0
        l, r = 0,0
        steps = 0
        while r < len(nums)-1:
            for i in range(l, r+1):
                reach = i + nums[i]
                if reach > maxReach: 
                    maxReach = reach
            l = r + 1
            r = maxReach
            steps += 1
        return steps