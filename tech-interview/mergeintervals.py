# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x: (x.start, x.end))
        ans = []
        cur = Interval(-1, -1)
        for i in range(len(intervals)):
            interval = intervals[i]
            if interval.start <= cur.end:
                cur.end = max(interval.end, cur.end)
            else:
                ans.append(cur)
                cur = Interval(interval.start, interval.end)
        ans += [cur]
        return ans[1:]