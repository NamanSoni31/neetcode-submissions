class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for i in range(len(s)): 
            d[s[i]] = i
        
        size = 0
        end = 0
        output = []
        for i in range(len(s)):
            size += 1
            val = d[s[i]]
            if val > end: 
                end = val
            if i == end: 
                output.append(size)
                size = 0
        return output