class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        minl = [prices[i] for i in range(len(prices))]
        for i in range(1, len(prices)):
            minl[i] = min(minl[i], minl[i - 1])
        res = 0
        for i in range(len(prices)):
            res = max(res, prices[i] - minl[i])
        return res
