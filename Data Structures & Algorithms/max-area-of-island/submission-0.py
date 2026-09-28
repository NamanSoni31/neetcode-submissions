class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: 
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        maxArea = 0
        
        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            count = 1
            while q:
                row, col = q.popleft()
                direction = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in direction: 
                    r = row + dr
                    c = col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r,c) not in visited:
                        q.append((r,c))
                        visited.add((r,c))
                        count += 1
            return count

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited: 
                    val = bfs(r,c)
                    maxArea = max(maxArea, val)
        return maxArea
