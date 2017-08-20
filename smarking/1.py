# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key=lambda x: (x.end, x.start))
        ans = 0
        r = -1
        for i in range(len(intervals)):
            il, ir = intervals[i].start, intervals[i].end
            if (r == -1) or il >= r:
                r = ir
            else:
                ans += 1
        return ans
