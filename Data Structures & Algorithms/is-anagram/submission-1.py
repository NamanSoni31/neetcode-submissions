class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
        
        for i in range(len(t)):
            if t[i] not in d: 
                return False
            if d[t[i]] == 0:
                return False
            d[t[i]] -= 1

        return True