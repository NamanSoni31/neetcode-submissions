class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adj = {i: [] for i in range(n)}

        if not n: 
            return True

        for n1, n2 in edges: 
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def dfs(curr, prev):
            if curr in visited: 
                return False
            visited.add(curr)
            for j in adj[curr]:
                if j == prev: 
                    continue
                if not dfs(j, curr):
                    return False
            return True

        return dfs(0,-1) and n == len(visited)