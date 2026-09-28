class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            dist = (-1) * (math.sqrt((points[i][0] ** 2) + (points[i][1] ** 2)))
            heapq.heappush(heap, [dist, points[i]])
            if len(heap) > k: 
                heapq.heappop(heap)

        return [pair[1] for pair in heap]