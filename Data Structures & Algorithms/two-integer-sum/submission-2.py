class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        smaller = 0
        bigger = 0
        for i in range(len(nums)):
            d[nums[i]] = i
        
        for j in range(len(nums)):
            x = target - nums[j]
            if x in d:
                if d[x] != j:
                    bigger = d[x]
                    smaller = j
                    return [smaller, bigger]