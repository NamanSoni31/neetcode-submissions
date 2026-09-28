class Solution:
    def isValid(self, s: str) -> bool:
        d = {}
        stack = deque()
        for i in range(len(s)):
            if s[i] in {'(', '{', '['}:
                stack.append(s[i])
                print(s[i])
            else:
                if len(stack) == 0: 
                    return False
                else: 
                    value = stack.pop()
                    if s[i] == ')':
                        if value != '(':
                            return False
                    elif s[i] == '}':
                        if value != '{':
                            return False
                    elif s[i] == ']':
                        if value != '[':
                            return False
        if len(stack) == 0:
            return True
        else: 
            return False