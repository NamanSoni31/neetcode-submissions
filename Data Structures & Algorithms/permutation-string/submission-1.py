class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        a = [0] * 26
        v = [0] * 26
        for k in s1:
            letter = ord(k) - 97
            a[letter] += 1
        y = 0
        while y in range(len(s2)):
            j = y
            while j < len(s2) and a[ord(s2[j]) - 97] > 0:
                let = ord(s2[j]) - 97
                v[let] += 1
                if v[let] <= a[let]:
                    j += 1
                else: 
                    break
            if j - y == len(s1):
                return True
            else: 
                y += 1
                v = [0] * 26
        return False
