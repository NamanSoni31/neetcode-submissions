import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        s = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        for i in range(len(tokens)):
            if tokens[i] in s:
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(int(s[tokens[i]](v2,v1)))
            else:
                stack.append(int(tokens[i]))

        return stack.pop()