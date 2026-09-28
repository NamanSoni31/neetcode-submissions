class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = [False, False, False]
        for i in range(len(triplets)):
            if triplets[i][0] > target[0] or triplets[i][1] > target[1] or triplets[i][2] > target[2]:
                    continue
            if triplets[i][0] == target[0]:
                found[0] = True
            if triplets[i][1] == target[1]:
                found[1] = True
            if triplets[i][2] == target[2]:
                found[2] = True
        if found[0] and found[1] and found[2]:
            return True
        return False
        