class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
        topK = sorted(d.items(), key = lambda x: x[1], reverse = True) [:k]
        topVals = sorted(d, key = d.get, reverse = True)[:k]
        return topVals