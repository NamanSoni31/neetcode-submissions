class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = [1]
        d = {}
        i = 0
        j = i
        if not s: 
            return 0 
        while j < len(s):
            if s[j] in d:
                longest.append(j - i)
                i = max(i, d[s[j]] + 1)
                d[s[j]] = j
                j += 1
            else: 
                d[s[j]] = j
                j += 1
                if j == len(s):
                    longest.append(j - i)
        return max(longest)