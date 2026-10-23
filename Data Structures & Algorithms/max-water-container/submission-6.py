class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxval = 0
        i = 0
        j = len(heights) - 1
        while i < j: 
            area = (j - i) * min(heights[i], heights[j])
            maxval = area if area > maxval else maxval
            if heights[i] <= heights[j]: 
                i += 1
            else: 
                j -= 1
        
        return maxval