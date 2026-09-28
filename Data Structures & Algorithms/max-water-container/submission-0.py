class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        for i in range(len(heights)-1):
            j = i + 1
            while j < len(heights):
                width = j - i
                height = min(heights[i],heights[j])
                if width*height > largest: 
                    largest = width * height
                    print(f"{i}, {j}, {width}, {height}")
                j += 1
        return largest