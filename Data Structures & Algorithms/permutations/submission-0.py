class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for i in nums: 
            new_perms = []
            for p in perms: 
                for j in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(j, i)
                    new_perms.append(p_copy)
            perms = new_perms
        return perms