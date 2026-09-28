class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(index, val):
            if val == target:
                res.append(subset.copy())
                return
            elif val > target or index == len(nums): 
                return
            else: 
                subset.append(nums[index])
                dfs(index, val + nums[index])
                subset.pop()
                dfs(index + 1, val)
        dfs(0, 0)
        return res