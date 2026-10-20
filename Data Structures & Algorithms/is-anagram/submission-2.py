class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        if len(s) != len(t):
            return False

        for char in s:
            d[char] = 1 + d.get(char, 0)
        
        for i in range(len(t)):
            if t[i] not in d: 
                return False
            if d[t[i]] == 0:
                return False
            d[t[i]] -= 1

        return True