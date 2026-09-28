class Solution:
    def longestPalindrome(self, s: str) -> str:
        resSize = 0
        res = 0
        
        def expand(start, end):
            if s[start] == s[end]:
                while (start - 1 >= 0 and end + 1 < len(s)) and s[start - 1] == s[end + 1]:
                    start -= 1
                    end += 1
                return start, end
            return start, start

        for i in range(len(s)):
            start, end = expand(i, i)
            if i + 1 < len(s):
                start1, end1 = expand(i, i + 1)
                if end1 - start1 + 1 > resSize: 
                    resSize = end1 - start1 + 1
                    res = start1
            if end - start + 1 > resSize: 
                resSize = end - start + 1
                res = start
        
        return s[res: res + resSize]
                
