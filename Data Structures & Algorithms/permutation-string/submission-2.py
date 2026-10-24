class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2 or len(s1) > len(s2):
            return False
        s = {}
        for i in s1:
            if i in s: 
                s[i] += 1
            else: 
                s[i] = 1

        j = 0
        k = j + 1
        scheck = {}
        scheck[s2[j]] = 1
        while j <= len(s2) - len(s1):
            while k - j < len(s1):
                if s2[k] not in scheck:
                    scheck[s2[k]] = 1
                else:
                    scheck[s2[k]] += 1
                k += 1
            
            if s == scheck:
                return True
            scheck[s2[j]] -= 1
            if scheck[s2[j]] == 0:
                del scheck[s2[j]]
            j += 1

        return False