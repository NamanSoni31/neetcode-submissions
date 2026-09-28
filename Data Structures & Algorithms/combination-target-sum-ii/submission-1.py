class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()
        def dfs(index, val):
            if val == target:
                if subset not in res:
                    res.append(subset.copy())
                return
            elif val > target or index == len(nums): 
                return
            else: 
                subset.append(nums[index])
                dfs(index + 1, val + nums[index])
                subset.pop()
                while (index + 1 < len(nums)) and nums[index + 1] == nums[index]:
                    index += 1
                dfs(index + 1, val)
        dfs(0, 0)
        return res