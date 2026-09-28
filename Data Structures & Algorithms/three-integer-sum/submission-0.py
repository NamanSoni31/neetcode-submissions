class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lst = []
        for i in range(len(nums)):
            val = 0 - nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] == val: 
                    lst.append([nums[i], nums[j], nums[k]])
                if nums[j] + nums[k] < val: 
                    j += 1
                else: 
                    k -= 1
        final = list(set(tuple(triplet) for triplet in lst))
        return final