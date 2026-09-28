class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0
        for i in range(len(s)):
            if s[i] == "(":
                low += 1
                high +=1
            if s[i] == ")":
                low -= 1
                high -= 1
                low = max(low, 0)
            if s[i] == "*":
                high += 1
                low -= 1
                low = max(low, 0)
            if high < 0: 
                return False

        if low != 0:
            return False
        return True