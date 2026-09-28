class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        rocks = []
        for i in range(len(stones)):
            heapq.heappush(rocks, (-1) * stones[i])
        
        while len(rocks) > 1: 
            r1 = heapq.heappop(rocks)
            r2 = heapq.heappop(rocks)
            if r1 != r2:
                heapq.heappush(rocks, r1 - r2)

        return -rocks[0] if rocks else 0