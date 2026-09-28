class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def expand(start, end):
            num = 0
            while (start >= 0 and end < len(s) and s[start] == s[end]):
                num += 1
                start -= 1
                end += 1
            return num
        
        for i in range(len(s)):
            res += expand(i, i)
            if i + 1 < len(s):
                res += expand(i, i +1)
        
        return res