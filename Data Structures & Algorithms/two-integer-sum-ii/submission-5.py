class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            x = target - numbers[i]
            ind = self.binarySearch(numbers, x, len(numbers) - 1, i + 1) 
            print(ind)
            if (numbers[ind] == x):
                return [i+1, ind+1]
    

    def binarySearch(self, numbers: List[int], x: int, hi, lo) -> int: 
        while lo < hi:
            mid = (lo + hi)//2

            if numbers[mid] == x:
                return mid
            if numbers[mid] < x:
                lo = mid + 1
            else: 
                hi = mid
        return lo