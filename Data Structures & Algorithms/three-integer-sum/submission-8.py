class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums = sorted(nums)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                val = nums[i] + nums[j] + nums[k]
                if val > 0: 
                    k -= 1
                elif val < 0:
                    j += 1
                else: 
                    triplets.add((nums[i], nums[j], nums[k]))
                    k -= 1
                    j += 1
                
        return list(triplets)