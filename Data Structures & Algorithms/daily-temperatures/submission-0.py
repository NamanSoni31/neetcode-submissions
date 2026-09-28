class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            stack = []
            for j in range(i, len(temperatures)):
                if temperatures[j] <= temperatures[i]:
                    stack.append(temperatures[j])
                    print(f"appended {temperatures[j]}, i = {i} and j = {j}")
                elif temperatures[j] > temperatures[i]:
                    res[i] = len(stack)
                    break
        return res