class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        rocks = []
        for i in range(len(stones)):
            heapq.heappush(rocks, (-1) * stones[i])
        
        while len(rocks) > 1: 
            r1 = heapq.heappop(rocks)
            r2 = heapq.heappop(rocks)
            diff = abs(r1 - r2) 
            if diff != 0:
                heapq.heappush(rocks, (-1) * diff)
        if len(rocks) == 0:
            heapq.heappush(rocks, 0)

        return abs(rocks[0])