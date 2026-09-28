class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(len(intervals)): 
            if intervals[i][0] > end:
                res.append(intervals[i-1])
            elif start > intervals[i][1]: 
                res.append(intervals[i-1])
            else: 
                intervals[i] = [min(start, intervals[i][0]), max(end, intervals[i][1])]
            start = intervals[i][0]
            end = intervals[i][1]
        
        res.append(intervals[i])
        return res