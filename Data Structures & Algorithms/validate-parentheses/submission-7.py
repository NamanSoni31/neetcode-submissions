class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check = {')': '(', ']': '[', '}': '{'}
        
        for i in s: 
            if i in check: 
                if stack and stack[-1] == check[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
                
        return True if not stack else False