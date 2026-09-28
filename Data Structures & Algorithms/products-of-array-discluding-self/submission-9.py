class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lst = [1] * len(nums)
        nums_zeros = 0
        total_a = 1
        for i in range(len(nums)):
            lst[i] = total_a
            total_a = total_a * nums[i]
        total_b = 1
        for i in range(len(nums)-1, -1, -1): 
            lst[i] = lst[i] * total_b
            total_b = total_b * nums[i]
        return lst