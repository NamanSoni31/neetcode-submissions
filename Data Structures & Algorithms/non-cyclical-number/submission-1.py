class Solution:
    def isHappy(self, n: int) -> bool:
        def sumSquares(num):
            sum = 0
            while num > 0:
                sum += (num % 10)**2
                num = num // 10
            
            return sum

        nums = set()
        
        while n not in nums and n != 1:
            nums.add(n)
            n = sumSquares(n)
        
        if n == 1: 
            return True
        
        return False