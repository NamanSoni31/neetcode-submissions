class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = {}
        adj = {i: [] for i in range(1,n+1)}

        for edge in times:
            adj[edge[0]].append((edge[1], edge[2]))
        
        min_heap = [(0, k)]
        while min_heap: 
            dist, node = heapq.heappop(min_heap)
            if node in visited: 
                continue
            for neighbor, weight in adj[node]:
                heapq.heappush(min_heap, (dist + weight, neighbor))
            visited[node] = dist
            

        if len(visited) == n:
            return max(visited.values())
        return -1