class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = n
        for i in range(1, n + 1):
            sum -= i
            if sum == 0:
                return i
            if sum < 0:
                return i - 1
        return 0
