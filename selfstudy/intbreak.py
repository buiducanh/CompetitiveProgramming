class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [i for i in range(n)]
        dp.append(1)
        for i in range(2, n + 1):
            if i == n:
                left = 1
            else:
                left = 0
            for k in range(left, (i+1)/2 + 1):
                dp[i] = max(dp[k] * dp[i - k], dp[i])
        return dp[n]
