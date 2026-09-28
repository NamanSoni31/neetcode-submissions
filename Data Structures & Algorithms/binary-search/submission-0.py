class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            ind = l + ((r - l) // 2)
            if nums[ind] == target: 
                return ind
            elif nums[ind] < target:
                l = ind + 1
            else: 
                r = ind - 1
        return -1