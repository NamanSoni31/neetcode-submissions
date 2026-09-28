class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        start = 0
        trip_tank = 0
        for i in range(len(cost)):
            tank += gas[i] - cost[i]
            trip_tank += gas[i] - cost[i]
            if trip_tank < 0: 
                start = i + 1
                trip_tank = 0
        if tank < 0:
            return -1
        return start