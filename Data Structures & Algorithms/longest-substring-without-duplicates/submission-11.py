class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        i = 0
        j = i + 1
        maxlen = 1
        d = set(s[0])
        while j < len(s):
            while s[j] in d: 
                d.remove(s[i])
                i = i + 1
                val = 0
            else:
                d.add(s[j])
                j += 1
            maxlen = max(maxlen, (j - i))

        return maxlen