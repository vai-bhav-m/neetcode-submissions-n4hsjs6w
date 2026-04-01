"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        def sortIntervals(intervals):
            if len(intervals) <= 1:
                return intervals
        
            pivot = intervals[len(intervals) // 2]
        
            left = [x for x in intervals if x.start < pivot.start]
            middle = [x for x in intervals if x.start == pivot.start]
            right = [x for x in intervals if x.start > pivot.start]
            
            return sortIntervals(left) + middle + sortIntervals(right)

        sorted_intervals = sortIntervals(intervals)
        for i in range(len(intervals) - 1):
            if sorted_intervals[i].end > sorted_intervals[i+1].start:
                return False
        return True