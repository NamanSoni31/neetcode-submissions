class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1: 
            r1 = heapq.heappop(stones)
            r2 = heapq.heappop(stones)
            if r1 != r2:
                heapq.heappush(stones, r1 - r2)
            
        return abs(stones[0]) if stones else 0