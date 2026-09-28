"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        max_cols = 0
        starting = [intervals[i].start for i in range(len(intervals))]
        starting.sort()
        ending = [intervals[i].end for i in range(len(intervals))]
        ending.sort()
        s = 0
        e = 0
        count = 0
        while s < len(starting) and e < len(starting):
            if ending[e] > starting[s]:
                count += 1
                max_cols = max(max_cols, count)
                s += 1
            else: 
                e += 1
                count -= 1
        return max_cols