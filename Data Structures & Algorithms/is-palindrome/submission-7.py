class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while j > i:
            while (i < j) and (not s[i].isalnum()):
                i += 1
                print("i incd")

            while (j > i) and (not s[j].isalnum()):
                j -= 1
                print("j decd")

            if s[i].lower() != s[j].lower():
                print(s[i])
                print(s[j])
                print(i,j)
                return False
            i += 1
            j -= 1
        
        return True