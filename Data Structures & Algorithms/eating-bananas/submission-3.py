import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        sortedList = sorted(piles)
        l = 1
        r = sortedList[-1]
        minVal = sortedList[-1]
        while l <= r:
            mid = (l + r) // 2
            hours = self.eachEatingSpeed(sortedList, mid)
            if hours <= h:
                r = mid - 1
                if mid < minVal:
                    minVal = mid
            else:
                l = mid + 1
        return minVal

    def eachEatingSpeed(self, piles: List[int], speed: int) -> int:
        hours = 0
        for i in range(len(piles)):
            hours = hours + math.ceil(piles[i] / speed)
        
        return hours
        #Gives the number of hours for each of the speeds possible in the list