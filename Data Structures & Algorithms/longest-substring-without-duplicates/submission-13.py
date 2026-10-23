class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        i = 0
        j = i + 1
        maxlen = 1
        d = {}
        d[s[0]] = 0
        while j < len(s):
            if s[j] in d: 
                i = max(i, d[s[j]] + 1)
                
            d[s[j]] = j
            j += 1
            maxlen = max(maxlen, (j - i))

        return maxlen