class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero_count = 0
        lst = [0]*len(nums)
        for i in range(len(nums)):
            if (nums[i] != 0):
                total = total * nums[i]
            else:
                zero_count += 1
                
        
        for i in range (len(nums)):
            if (zero_count > 0):
                if(nums[i] == 0 and zero_count == 1):
                    lst[i] = total
                else: 
                    lst[i] = 0
            else: 
                lst[i] = int(total/nums[i])

        return lst