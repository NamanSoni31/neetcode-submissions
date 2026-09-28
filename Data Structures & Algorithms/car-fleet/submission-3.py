class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ordCars = {}
        for i in range(len(position)):
            ordCars[position[i]] = speed[i]
        ordCars = sorted(ordCars.items(), key=lambda x: x[0], reverse=True)

        stack = []
        for i in range(len(ordCars)):
            time = (target - ordCars[i][0]) / ordCars[i][1]
            if stack: 
                if time > stack[-1]:
                    stack.append(time)
            else:
                stack.append(time)
        return len(stack)