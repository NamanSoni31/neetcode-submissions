class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = {}
        def time(position, speed):
            return (target - position) / speed

        for i in range(len(position)): 
            cars[position[i]] = time(position[i], speed[i])

        car_times_sorted = sorted(cars.items(), reverse = True)
        count = 1
        stack = []
        
        for pos, time in car_times_sorted:
            if stack:
                t1 = stack[-1]
                if t1 < time: 
                    count += 1
                    stack.append(time)
            else:
                stack.append(time)
        
        return count