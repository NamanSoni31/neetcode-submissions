import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        toks = ['+', '-', '*', '/']
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }
        for i in range(len(tokens)):
            if tokens[i] not in toks: 
                stack.append(tokens[i])
                print(f"appended {tokens[i]}")
            else:
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(ops[tokens[i]](int(v2), int(v1)))
                print(f"merged in stack to : {stack}")
        return int(stack[0])