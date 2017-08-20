# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        import bisect
        ans = [-1 for i in intervals]
        starts = [i for i in range(len(intervals))]
        starts.sort(key=lambda x: intervals[x].start)
        startVals = [intervals[i].start for i in starts]


        for i in range(len(intervals)):
            interval = intervals[i]
            index = bisect.bisect_left(startVals, interval.end)
            if index < len(starts):
                ans[i] = starts[index]
        return ans
