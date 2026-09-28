class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = []
        def dfs(open, close):
            if open == close and open == n: 
                res.append("".join(subset.copy()))
                return
            if open > close: 
                subset.append(')')
                dfs(open, close + 1)
                subset.pop()
            if open < n: 
                subset.append('(')
                dfs(open + 1, close)
                subset.pop()
        dfs(0, 0)
        return res