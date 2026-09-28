class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        vol = 0
        while i < j:
            height = min(heights[i], heights[j])
            width = j - i
            vol = max(height*width,vol)
            if heights[i] >= heights[j]:
                j -= 1
            elif heights[i] < heights[j]:
                i += 1
        
        return vol