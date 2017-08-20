# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while l < r:
            mid = (r - l) / 2 + l
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        if isBadVersion(l):
            return l
        else:
            return None