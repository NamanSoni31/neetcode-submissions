class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        if len(s) != len(t):
            return False

        for char in s:
            d[char] = 1 + d.get(char, 0)
        
        for i in t:
            if i not in d: 
                return False
            if d[i] == 0:
                return False
            d[i] -= 1

        return True