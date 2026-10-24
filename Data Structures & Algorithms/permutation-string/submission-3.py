class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        m = len(s1)
        a = [0] * 26
        b = [0] * 26

        for i in range(m):
            a[ord(s1[i]) - ord('a')] += 1
            b[ord(s2[i]) - ord('a')] += 1
        
        if a == b: 
            return True
        
        for i in range(m, len(s2)):
            b[ord(s2[i]) - ord('a')] += 1
            b[ord(s2[i - m]) - ord('a')] -= 1

            if a == b: 
                return True
        
        return False
