class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = {}

        for i in range(len(position)): 
            cars[position[i]] = (target - position[i]) / speed[i]

        car_times_sorted = sorted(cars.items(), reverse = True)
        stack = []
        
        for pos, time in car_times_sorted:
            if stack:
                t1 = stack[-1]
                if t1 < time: 
                    stack.append(time)
            else:
                stack.append(time)
        
        return len(stack)